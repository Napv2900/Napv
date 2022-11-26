from moviepy.editor import *
def f():
    from PIL import Image, ImageDraw, ImageFont
    import os
    for i in range(10):
        text=str(input("Введите текст:\n"))
        im = Image.new('RGB', (1000,1000), color="#99CC00")
        font=ImageFont.truetype('C:/Windows/Fonts/micross.ttf', size=18)
        draw_text=ImageDraw.Draw(im)
        draw_text.text((100,100), text, font=font, fill='#1C0606')
        im.save(f'C:/Users/student/Documents/142/Наумов/26.11.22/{i}.jpg')
    directory='C:/Users/student/Documents/142/Наумов/26.11.22'
    files=os.listdir(directory)
    image=list(filter(lambda x: x.endswith('.jpg'), files))
    clips = [ImageClip(m).set_duration(2) for m in image]
    final_clip=concatenate_videoclips(clips, method='compose')
    final_clip.write_videofile('movie.mp4', fps=24)        
f()
        
