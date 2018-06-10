import Tkinter as tk
'''
September 24, 2017

polyciUI v1, A ui for the polyci program.
-Numerator

'''


class polyciUI:
	def __init__(self, parent, *args, **kwargs):
		self.parent = parent
		self.parent.title("polyciUI")
		self.parent.geometry("500x400")
		self.parent.wm_attributes("-topmost", True)
		center(self.parent, y_add=-40)
		
		self.mframe = tk.Frame(self.parent, bg="green")
		self.mframe.pack(expand=1, fill=tk.BOTH)
		
		# button frame and text
		self.bframe = tk.Frame(self.mframe, bg="#1e8931")
		self.bframe.pack(fill=tk.X)
		self.text1 = tk.Text(self.mframe, padx=5, pady=5, font="Helvetica 12", bg="#776f3d")
		self.text1.pack(expand=1, fill=tk.BOTH)
		
		# 3 buttons
		self.bEn = tk.Button(self.bframe, text="Encrypt", width=15, 
			relief=tk.SOLID, command=self.mode_switch, bg="#1e8931")
		self.bEn.pack(side=tk.LEFT, padx=2, pady=(1, 1))
		self.bGo = tk.Button(self.bframe, text="Go", width=7, relief=tk.SOLID,
			command=self.crypt, bg="#1e8931")
		self.bGo.pack(side=tk.RIGHT, padx=(5, 2), pady=(1, 1))
		self.bCA = tk.Button(self.bframe, text="Clear Text", width=10, 
			relief=tk.SOLID, command=self.clear_text, bg="#1e8931")
		self.bCA.pack(side=tk.RIGHT, pady=(1, 1))
		
		# key entry
		tk.Label(self.bframe, text="Key: ", width=3, anchor=tk.W, bg="#1e8931").pack(side=tk.LEFT, 
			padx=2, pady=(0, 1))
		self.eKy = tk.Entry(self.bframe, width=15, font="Helvetica 12 bold")
		self.eKy.pack(side=tk.LEFT, padx=2, pady=(2, 1))
		self.bEC = tk.Button(self.bframe, text="[X]", width=3, 
			relief=tk.SOLID, command=self.clear_entry, bg="#1e8931")
		self.bEC.pack(side=tk.LEFT, padx=2, pady=(1, 1))
		
	
	def mode_switch(self, *args):
		if self.bEn["text"] == "Encrypt":
			self.bEn["text"] = "[[[Decrypt]]]"
		else:
			self.bEn["text"] = "Encrypt"
	
	
	def crypt(self, *args):
		key = self.eKy.get()
		text = self.text1.get(1.0, tk.END)
		ct = polyci()
		mtext = ""
		if key != "":
			if self.bEn["text"] == "Encrypt":
				mtext = ct.codec(key, text)
			else:
				mtext = ct.codec(key, text, 1)
		else:
			mtext = "Insert key."
		self.text1.delete("1.0", tk.END)
		self.text1.insert(tk.END, mtext)
		
	
	def clear_text(self, *args):
		self.text1.delete("1.0", tk.END)
		
	
	def clear_entry(self, *args):
		self.eKy.delete("0", tk.END)


class polyci:
	def __init__(self, *args, **kwargs):
		self.alphabet = [ # 79
			'a', 'b', 'c', 'd', 'e', 'f', 'g',
			'h', 'i', 'j', 'k', 'l', 'm', 'n',
			'o', 'p', 'q', 'r', 's', 't', 'u',
			'v', 'w', 'x', 'y', 'z',
			'A', 'B', 'C', 'D', 'E', 'F', 'G',
			'H', 'I', 'J', 'K', 'L', 'M', 'N',
			'O', 'P', 'Q', 'R', 'S', 'T', 'U',
			'V', 'W', 'X', 'Y', 'Z',
			'1', '2', '3', '4', '5', '6', '7',
			'8', '9', '0',
			'!', '@', '#', '$', '%', '^', '&',
			'*', '(', ')',
			',', '.', '<', '>', '?', '/', ' '
		]
	
	
	def codec(self, key, msg, mode=0):
		''' Returns encrypted/decrypted text.
		
		key -- only characters from the alphabet list.
		msg -- the plaintext/ciphertext.
		mode -- encrypt 0/decrypt 1.
		'''
		kletters = [] # position of key elements
		for letter in key:
			if letter in self.alphabet:
				kletters.append(self.alphabet.index(letter))
			else:
				return "Error, Key Invalid."
		
		modtext = ""
		kplace = 0 # key element number.
		for letter in msg:
			if letter in self.alphabet:
				cletter = self.alphabet.index(letter)
				ops = kletters[kplace] * (1 if mode==1 else -1)
				fletter = cletter - ops
				if fletter >= len(self.alphabet):
					fletter -= len(self.alphabet)
				modtext += self.alphabet[fletter]
				kplace += 1 # switch key elements
				if kplace >= len(key):
					kplace = 0
			else:
				modtext += letter
				
		return modtext	
		

def center(win, x_add=0, y_add=0):
	win.update_idletasks()
	width = win.winfo_width()
	height = win.winfo_height()
	x = (win.winfo_screenwidth() // 2) - (width // 2)
	y = (win.winfo_screenheight() // 2) - (height // 2)
	win.geometry('{}x{}+{}+{}'.format(width, height, x+x_add, y+y_add))
	

if __name__ == "__main__":
	root = tk.Tk()
	app = polyciUI(root)
	root.mainloop()