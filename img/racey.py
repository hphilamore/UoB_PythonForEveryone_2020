import io
import base64
from IPython.display import HTML





def play_vid():
	video = io.open('img/pygame-tutorials.mp4', 'r+b').read()
	encoded = base64.b64encode(video)

	HTML(data='''<video width = "500"  alt="test" controls>
	                <source src="data:video/mp4;base64,{0}" type="video/mp4" />
	             </video>'''.format(encoded.decode('ascii')))

