import cv2
import os

def convert_mov_to_mp4(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.mov'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.mp4'
            output_path = os.path.join(output_folder, output_filename)
            
            print(f"Converting: {input_path} -> {output_path}")
            cap = cv2.VideoCapture(input_path)
            
            if not cap.isOpened():
                print(f"Error opening video file: {input_path}")
                continue
            
            # Get video properties
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            # Define the codec and create VideoWriter object.
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)
            
            cap.release()
            out.release()
            print(f"Finished converting {filename}")

if __name__ == '__main__':
    input_folder = r'C:\Users\Parker Manson\Downloads\new training\New folder\download (1)'      # Update with your input folder path
    output_folder = r'C:\Users\Parker Manson\Downloads\new training\New folder\download (1)'       # Update with your output folder path
    
    convert_mov_to_mp4(input_folder, output_folder)
