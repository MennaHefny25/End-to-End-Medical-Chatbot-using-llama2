# End-to-End-Medical-Chatbot-using-llama2

## Steps to run the project

#### 1) Create virtual environment 
```bash
$ conda create -n `environment_name` python=3.10 -y
```

#### 2) Activate environment 
```bash
$ conda activate `environment_name`
```

### 3) Install requirements  
```bash
$ pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:
```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python main.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone

