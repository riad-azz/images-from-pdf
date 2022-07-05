from os import path, mkdir
from threading import Thread
import fitz


class ImageExtractor:
    def __init__(self, master):
        self.master = master

    def extract(self, file_path, save_path):
        thread = Thread(target=self._extract, args=[file_path, save_path])
        thread.start()

    def _extract(self, file_path, save_path):
        file = file_path
        pdf_file = fitz.Document(file)

        # Create save dir if it doesn't exist
        if not path.isdir(save_path):
            mkdir(save_path)

        # Count images
        img_count = 0
        for i in range(len(pdf_file)):
            img_count += len(pdf_file.get_page_images(i))

        # Cancel extraction if the pdf contains no images
        if img_count == 0:
            self.master.enable_all(done=False, error="No images found in this file")
            return

        curr_count = 0
        for i in range(len(pdf_file)):
            for j, img in enumerate(pdf_file.get_page_images(i)):
                curr_count += 1
                self.master.update_progress(img_count, curr_count)
                xref = img[0]
                pix = fitz.Pixmap(pdf_file, xref)
                if pix.colorspace is fitz.csCMYK:  # GRAY or RGB
                    pix.save(f"{save_path}/page_{i}_img_{j}.png")
                else:
                    # Convert to RGB
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                    pix.save(f"{save_path}/page_{i}_img_{j}.png")

        self.master.enable_all(True)
