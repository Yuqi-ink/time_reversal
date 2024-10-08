import imageio
import os

def images_to_video(image_folder, output_video, fps):
    images = sorted([img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")])
    frames = [imageio.v2.imread(os.path.join(image_folder, img)) for img in images]
    imageio.mimsave(output_video, frames, fps=fps)

if __name__ == "__main__":
    image_folder = 'output/gym_motion_exp/stable-video-diffusion-img2vid-xt_fps17_id10_s-num50_re9_5_2_1.0/arm_clip1_frame_00018_frame_00060'
    output_video = 'output/gym_motion_exp/stable-video-diffusion-img2vid-xt_fps17_id10_s-num50_re9_5_2_1.0/output_video.mp4'
    if "gym_motion" in image_folder:
        fps = 17
    else:
        fps = 7
    images_to_video(image_folder, output_video, fps)
    print(f"Video saved to {output_video}")
