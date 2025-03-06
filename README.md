# genetic-drift-simulation
# Sean Chien

This is the genetic drift simulation. The results will be save as PNG files in a directory. 

You can use  ffmpeg to convert to all pngs into and short video.


```bash
ffmpeg -framerate 30 -i frame_%03d.png -c:v libx264 -pix_fmt yuv420p -crf 18 output_video.mp4
```
