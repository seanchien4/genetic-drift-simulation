# genetic-drift-simulation
# Sean Chien

This is the genetic drift simulation. 
You can modify population size, generation, allele frequency.
The results will be save as PNG files in a directory. 

You can use  ffmpeg to convert to all pngs into and short video.


```bash
ffmpeg -framerate 30 -i frame_%03d.png -c:v libx264 -pix_fmt yuv420p -crf 18 output_video.mp4
```


This is population size = 50 with 300 generations.
https://github.com/user-attachments/assets/cfb1f1ff-a0a3-4dc7-99bb-537b52cb2e78


This is population size = 5000 with 300 generations.
https://github.com/user-attachments/assets/f366f175-1f87-481e-8307-e4b4f1eabc38

