from transformers import pipeline
Strip_text = open('sentences.txt').read().split('\n')
masker = pipeline('fill-mask', model='roberta-base')
masker(Strip_text)
