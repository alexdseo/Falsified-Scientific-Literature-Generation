# Generated Fake Texts from Grover

**Run `get_text.ipynb` to extract the newly generated fake text to .txt file which are all saved in `fake_text` folder and write a `*_disc.jsonl` file that could be feed right into the Grover discriminator.**

- falsified_text_fromBIK*.jsonl are output files you will get after running `grover.ipynb` (at least without any change, feel free to change the name of the output file if you are using other data to generate fake texts). This file contains every metadata from the original input paper along with the new generated article. 

- The `test_with_GROVER_large` folder contains result from using pretrained model instead of base model that we mainly used which you could download from `download_model.py`. 
