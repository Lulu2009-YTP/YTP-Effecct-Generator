import tkinter as tk
from tkinter import ttk, filedialog
from moviepy.editor import *
import random
import numpy as np

class YTPEffectsGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Poop Effects Generator")
        
        # Input/Output paths
        self.input_path = ""
        self.output_path = ""
        
        self.create_gui()
    
    def create_gui(self):
        # File Selection Frame
        file_frame = ttk.LabelFrame(self.root, text="File Selection", padding=10)
        file_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        
        ttk.Button(file_frame, text="Select Input Video", command=self.select_input).grid(row=0, column=0, padx=5)
        ttk.Button(file_frame, text="Select Output Location", command=self.select_output).grid(row=0, column=1, padx=5)
        
        # Effects Frame
        effects_frame = ttk.LabelFrame(self.root, text="Effects", padding=10)
        effects_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        self.effects = {
            "Sentence Mixing": tk.BooleanVar(value=True),
            "Reverse": tk.BooleanVar(value=True),
            "Speed Changes": tk.BooleanVar(value=True),
            "Color Distortion": tk.BooleanVar(value=True),
            "Stutter Effect": tk.BooleanVar(value=True)
        }
        
        for i, (effect, var) in enumerate(self.effects.items()):
            ttk.Checkbutton(effects_frame, text=effect, variable=var).grid(row=i, column=0, sticky="w")
        
        # Generate Button
        ttk.Button(self.root, text="Generate YTP", command=self.generate_ytp).grid(row=2, column=0, pady=10)
    
    def select_input(self):
        self.input_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.mkv")]
        )
    
    def select_output(self):
        self.output_path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("MP4 files", "*.mp4")]
        )
    
    def apply_sentence_mixing(self, clip):
        # Split audio into segments and randomly rearrange
        if len(clip.duration) < 2:
            return clip
        
        segments = []
        segment_duration = 0.5
        for t in np.arange(0, clip.duration, segment_duration):
            if t + segment_duration > clip.duration:
                break
            segments.append(clip.subclip(t, t + segment_duration))
        
        random.shuffle(segments)
        return concatenate_videoclips(segments)
    
    def apply_reverse(self, clip):
        return clip.fl_time(lambda t: clip.duration - t)
    
    def apply_speed_changes(self, clip):
        return clip.speedx(random.uniform(0.5, 2.0))
    
    def apply_color_distortion(self, clip):
        return clip.fl_image(lambda frame: np.uint8(255 * (frame/255.0)**random.uniform(0.8, 1.2)))
    
    def apply_stutter(self, clip):
        if clip.duration < 0.5:
            return clip
            
        stutter_time = random.uniform(0, clip.duration - 0.5)
        stutter_duration = 0.2
        stutter_segment = clip.subclip(stutter_time, stutter_time + stutter_duration)
        stutter_repeated = concatenate_videoclips([stutter_segment] * 3)
        
        return CompositeVideoClip([
            clip,
            stutter_repeated.set_start(stutter_time)
        ])
    
    def generate_ytp(self):
        if not self.input_path or not self.output_path:
            tk.messagebox.showerror("Error", "Please select input and output files")
            return
            
        try:
            video = VideoFileClip(self.input_path)
            
            # Apply selected effects
            if self.effects["Sentence Mixing"].get():
                video = self.apply_sentence_mixing(video)
            if self.effects["Reverse"].get():
                video = self.apply_reverse(video)
            if self.effects["Speed Changes"].get():
                video = self.apply_speed_changes(video)
            if self.effects["Color Distortion"].get():
                video = self.apply_color_distortion(video)
            if self.effects["Stutter Effect"].get():
                video = self.apply_stutter(video)
            
            # Write the final video
            video.write_videofile(self.output_path, codec='libx264', audio_codec='aac')
            video.close()
            
            tk.messagebox.showinfo("Success", "YTP generation complete!")
            
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YTPEffectsGenerator(root)
    root.mainloop()