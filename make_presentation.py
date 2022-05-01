from pptx import Presentation 
from datetime import datetime
import os
X = Presentation()
Layout = X.slide_layouts[0] 
first_slide = X.slides.add_slide(Layout) # Adding first slide
print("Enter the title of your presentation: ")
input_str = str(input())
first_slide.shapes.title.text = input_str
print("Enter the name of presenters:")
author_names = str(input())
first_slide.placeholders[1].text = "By " + author_names
now = datetime.now()
new_now = now.strftime("%H%M%S")
presentation_name = "new_presentation"+ str(new_now) + ".pptx"
X.save(presentation_name)
print("Starter presentation file successfully created!")
os.startfile(presentation_name)






 



