# pip install transformers

from transformers.utils import logging
logging.set_verbosity_error()

from transformers import pipeline
import torch
import gc

translator = pipeline(task="translation",
                      model="facebook/nllb-200-distilled-600M",
                      torch_dtype=torch.bfloat16) 

text = """\
My puppy is adorable, \
Your kitten is cute.
Her panda is friendly.
His llama is thoughtful. \
We all have nice pets!"""

text_translated = translator(text,
                             src_lang="eng_Latn",
                             tgt_lang="spa_Latn")

print(text_translated)

del translator
gc.collect()