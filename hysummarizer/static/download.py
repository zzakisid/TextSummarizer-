from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "sshleifer/distilbart-cnn-12-6"
save_directory = "E:/hysummarizer/model"  # Change to your preferred path

# Load the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model locally
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)

print("Model downloaded and saved successfully!")
