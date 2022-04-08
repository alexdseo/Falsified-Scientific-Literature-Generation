# Install Docker.
- https://docs.docker.com/get-docker

# Build Docker.
- `docker build -f Im2txtRestDockerfile -t uscdatascience/im2txt-rest-tika .`
- `docker run -it -p 8764:8764 uscdatascience/im2txt-rest-tika`

# Run `part6.py` on Terminal. Make sure unzipped `generated_images` in same directory.
- `python part6.py`
- Output file: `out.out`

# Run `caption_generation.ipynb` to parse `out.out` and generate `captions.txt`.
- `captions` saved as a list to be accessed in `data_preprocess/data_preprocess.ipynb`