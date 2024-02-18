# !!!
MODALITY_NOT_EXIST_ID = -1
IGNORE_ID = -100
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "<s>"
DEFAULT_UNK_TOKEN = "<unk>"
TOKENIZER_NAME_OR_PATH = 'yahma/llama-7b-hf'
TOKENIZER_SPECIAL_TOKENS = {
    "eos_token": DEFAULT_EOS_TOKEN,
    "bos_token": DEFAULT_BOS_TOKEN,
    "unk_token": DEFAULT_UNK_TOKEN,
}

# mean and variance for R, G, B channels
IMAGENET_DEFAULT_MEAN = [0.485, 0.456, 0.406]
IMAGENET_DEFAULT_STD = [0.229, 0.224, 0.225]
IMAGENET_STANDARD_MEAN = [0.5, 0.5, 0.5]
IMAGENET_STANDARD_STD = [0.5, 0.5, 0.5]
OPENAI_CLIP_MEAN = [0.48145466, 0.4578275, 0.40821073]
OPENAI_CLIP_STD = [0.26862954, 0.26130258, 0.27577711]
