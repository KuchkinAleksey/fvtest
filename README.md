# VIPE Gaussian Splatting Demo

3D Gaussian Splatting reconstruction of a drone survey, with camera poses estimated by
[ViPE](https://github.com/nv-tlabs/vipe).

## Build

### 1. Preprocess the photos

Downscaling only − smaller frames make the inference much faster. Set the constants at the
top of the script, then run it:

```python
INPUT = "zavod70/*"        # folder with the original DJI photos
OUTPUT = "data/zavod70"    # folder NAME becomes the ViPE sequence name
```

```bash
python prepare_dataset.py
```

Produces `frame_00000.jpg …` at 640×480.

### 2. Upload to Google Drive

Zip **the folder itself**, not its contents, and put it in a project folder on your Drive:

```
MyDrive/fvtest/zavod70.zip
```

### 3. Run the notebook in Colab

Open [vipe.ipynb](vipe.ipynb), set **Runtime → Change runtime type → GPU → A100**, and run the
cells top to bottom.

Check that `DRIVE_DIR` in the config cell matches your Drive folder:

```python
DRIVE_DIR = '/content/drive/MyDrive/fvtest'
```

The whole notebook takes about 45 minutes on an A100. Results are copied to
`MyDrive/fvtest/result/`.

## Results

Trained scene, 4.5M gaussians: [point_cloud.ply](https://drive.google.com/file/d/17w0S197DdMLPMfmaUc4q9p2cE_bjYfk8/view?usp=sharing)

Viewer [webgl-gaussian-splatting.vercel.app](https://webgl-gaussian-splatting.vercel.app/)

Preview
<img width="1919" height="1079" alt="preview1" src="https://github.com/user-attachments/assets/858ea3c6-49d4-412c-b212-9bfbee2ade29" />
<img width="1919" height="1079" alt="preview2" src="https://github.com/user-attachments/assets/daa17e3f-2c8d-4cd1-9de5-fc8ed1d4e600" />

Flight path


https://github.com/user-attachments/assets/64166781-b10e-41df-b6c6-4fc01e45aeac



Orbit path


https://github.com/user-attachments/assets/3e6fb8cc-9108-4bfe-8d9c-254e81cc0106


