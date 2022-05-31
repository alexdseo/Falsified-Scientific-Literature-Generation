# Falsified Scientific Literature Generation

Grover is a model that was introduced on [Defending Against Neural Fake News](https://arxiv.org/abs/1905.12616) that is designed to both generate and detect neural fake news. For this project, **Falsified Scientific Literature Generation**, we leverage the data that was created from [prior project](https://github.com/alexdseo/Semantic-Forensics-in-Scientific-Literature) and use it to generate fake scientific literature that is nearly undistinguishable from human written literature. Then, we attempt to see if the Grover discriminates the manipulated and plagiarised paper as a fake scientific literature.

For more information about Grover, visit original author's project page at [rowanzellers.com/grover](https://rowanzellers.com/grover), [the AI2 online demo](https://grover.allenai.org), or read the full paper at [arxiv.org/abs/1905.12616](https://arxiv.org/abs/1905.12616) and see the [original repo](https://github.com/rowanz/grover).

![teaser](https://i.imgur.com/VAGFpBe.png "teaser")

## Generating fake text using Grover

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com//github/alexdseo/Falsified-Scientific-Literature-Generation/blob/master/fake_text/grover.ipynb)

## Result

- [Example of generated fake paper](https://github.com/alexdseo/Falsified-Scientific-Literature-Generation/blob/master/LaTeX/fake_scientific_literature.pdf)

### Ideas for improvement

There were few areas that could use some improvement. For example, while Grover generated believable text, it did poorly on generating fake title which could be improved with a model that performs better on these tasks. We also used DCGAN to generate fake face of the authors, however, for the scientific papers it would be better if we also include scientific images that correspond with the fake texts. Finally, in classifying the fake and human written texts, Grover believed that on average, there is a 68.65% chance that a human-written paper from the Bik dataset was written by machines. We believe that this accuracy could be improved if the model is pretrained with the scientific literature instead of the news article which is what it was built for.


- [Generate Fake title using GPT-2](https://github.com/csinva/gpt2-paper-title-generator)
- Generate fake scientific images that would go well with a fake scientific paper (i.e. using Convolutional VAE)
     - [Generate caption of the image using Inception-v4](https://github.com/alexdseo/Falsified-Scientific-Literature-Generation/tree/master/caption_generation)
- Pre-train Grover based on scientific papers 

------------

### Bibtex

```
@inproceedings{zellers2019grover,
    title={Defending Against Neural Fake News},
    author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
    booktitle={Advances in Neural Information Processing Systems 32},
    year={2019}
}
```
