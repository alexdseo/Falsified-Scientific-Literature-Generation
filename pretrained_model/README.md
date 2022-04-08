# Using pre-trained Grover Model

## Checkpoints

[Download pretrained model checkpoint here](https://drive.google.com/drive/folders/1soN2XWoFQDZGp1a4lENG1mfEo4AVxNSr)

Or you can download from the repo, however, you do need to download `model.ckpt-1562.data` which is not in this repo.

- Download the files in the above google drive and save it in your own Google Drive account. To make sure you can use this model checkpoint while running  `grover.ipynb` using Google CoLab, Please set your google drive folder name where you saved all the files as `GROVER_pretrained` so you do not have to change anything in the CoLab file.

**NOTE**: These checkpoints were trained on 5000 examples from a specific Grover generator, with a specific nucleus sampling top-p setting. As a result, these aren't necessarily the best discrimination checkpoints, nor are they the most general. The reason we used this experimental setup is outlined [in the paper](https://arxiv.org/abs/1905.12616) -- we assumed limited access to the generator. We did [later experiments](https://medium.com/ai2-blog/counteracting-neural-disinformation-with-grover-6cf6690d463b) and found that if you assume, say, 100k examples from a generator, you'll do much better (up to around 97% accuracy).
