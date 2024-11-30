import torch
from torch.optim import AdamW
from torch.utils.data import DataLoader
from datasets import load_dataset
from transformers import RobertaTokenizer, RobertaForSequenceClassification, get_scheduler
from tqdm import tqdm

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

dataset = load_dataset("code_x_glue_cc_clone_detection_poj104")
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")

def preprocess_function(examples):
    examples['label'] = [int(label) for label in examples['label']]
    return tokenizer(examples['code'], padding="max_length", truncation=True, max_length=128)

tokenized_dataset = dataset.map(preprocess_function, batched=True)
train_data = tokenized_dataset['train']
val_data = tokenized_dataset['validation']
test_data = tokenized_dataset['test']

def collate_fn(batch):
    return {
        "input_ids": torch.stack([torch.tensor(item['input_ids']) for item in batch]),
        "attention_mask": torch.stack([torch.tensor(item['attention_mask']) for item in batch]),
        "labels": torch.tensor([int(item['label']) for item in batch])
    }

train_loader = DataLoader(train_data, batch_size=8, collate_fn=collate_fn, shuffle=True)
val_loader = DataLoader(val_data, batch_size=16, collate_fn=collate_fn)
test_loader = DataLoader(test_data, batch_size=16, collate_fn=collate_fn)

model = RobertaForSequenceClassification.from_pretrained("microsoft/codebert-base", num_labels=104)
model.to(device)

optimizer = AdamW(model.parameters(), lr=2e-5)
num_epochs = 3
num_training_steps = num_epochs * len(train_loader)
lr_scheduler = get_scheduler(name="linear", optimizer=optimizer, num_warmup_steps=0, num_training_steps=num_training_steps)

def train_model(model, train_loader, val_loader, epochs):
    model.train()
    training_stats = []
    
    for epoch in range(epochs):
        total_train_loss = 0
        correct_predictions = 0
        total_predictions = 0
        
        for batch in tqdm(train_loader, desc=f"Training Epoch {epoch+1}/{epochs}"):
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            loss = outputs.loss
            logits = outputs.logits
            
            loss.backward()
            optimizer.step()
            lr_scheduler.step()
            optimizer.zero_grad()
            
            total_train_loss += loss.item()
            
            _, preds = torch.max(logits, dim=1)
            correct_predictions += torch.sum(preds == batch["labels"]).item()
            total_predictions += len(preds)
        
        avg_train_loss = total_train_loss / len(train_loader)
        train_accuracy = correct_predictions / total_predictions
        val_loss, val_accuracy = evaluate_model(model, val_loader)

        print(f"\nEpoch {epoch+1}:")
        print(f"Training Loss: {avg_train_loss:.4f}, Training Accuracy: {train_accuracy:.4f}")
        print(f"Validation Loss: {val_loss:.4f}, Validation Accuracy: {val_accuracy:.4f}")

        training_stats.append({
            'epoch': epoch+1,
            'Training Loss': avg_train_loss,
            'Training Accuracy': train_accuracy,
            'Validation Loss': val_loss,
            'Validation Accuracy': val_accuracy
        })

    return training_stats

def evaluate_model(model, val_loader):
    model.eval()
    total_val_loss = 0
    correct_predictions = 0
    total_predictions = 0
    
    with torch.no_grad():
        for batch in val_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            loss = outputs.loss
            logits = outputs.logits
            
            total_val_loss += loss.item()

            _, preds = torch.max(logits, dim=1)
            correct_predictions += torch.sum(preds == batch["labels"]).item()
            total_predictions += len(preds)
    
    avg_val_loss = total_val_loss / len(val_loader)
    val_accuracy = correct_predictions / total_predictions

    return avg_val_loss, val_accuracy

training_stats = train_model(model, train_loader, val_loader, epochs=num_epochs)

print("\nTraining Complete!")
for stat in training_stats:
    print(f"Epoch {stat['epoch']}: Train Loss = {stat['Training Loss']:.4f}, Train Accuracy = {stat['Training Accuracy']:.4f}, Val Loss = {stat['Validation Loss']:.4f}, Val Accuracy = {stat['Validation Accuracy']:.4f}")
