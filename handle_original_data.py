import os
import shutil

dst="raw_data/val/"
source_path="dataset/val/"

match_list=os.listdir(source_path)
i=0
j=0
for match in match_list:
    if match.startswith('match'):
        video_path=source_path+match+"/rally_video/"
        ball_path=source_path+match+"/ball_trajectory/"

        video_list=os.listdir(video_path)
        ball_list=os.listdir(ball_path)

        video_list.sort()
        ball_list.sort()

        for video in video_list:
            i+=1
            if video.endswith('.mp4'):
                src=video_path+video
                shutil.move(src, dst)

                old_name=dst+video
                new_name=dst+str(i)+".mp4"
                os.rename(old_name, new_name)

        for ball in ball_list:
            j+=1
            if ball.endswith('.csv'):
                src=ball_path+ball
                shutil.move(src, dst)

                old_name=dst+ball
                new_name=dst+str(j)+".csv"
                os.rename(old_name, new_name)

    print(".", end='')

print('')
print("Finished!")