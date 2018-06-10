import tkinter as tk

class PolyciUI:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.parent.title("PolyciUI")
        self.parent.geometry("375x250")
        self.parent.wm_attributes("-topmost", True)
        center(self.parent, y_add=-40)
        
        self.mframe = tk.Frame(self.parent, bg="green")
        self.mframe.pack(expand=1, fill=tk.BOTH)
        
        # button frame and text
        self.bframe = tk.Frame(self.mframe, bg="#1e8931")
        self.bframe.pack(fill=tk.X)
        self.text1 = tk.Text(self.mframe, padx=5, pady=5,
            font="Helvetica 12", bg="#776f3d")
        self.text1.pack(expand=1, fill=tk.BOTH)
        
        # 3 buttons
        self.bEn = tk.Button(self.bframe, text="Encrypt", width=10, 
            relief=tk.SOLID, command=self.mode_switch, bg="#1e8931")
        self.bEn.pack(side=tk.LEFT, padx=2, pady=(1, 1))
        self.bGo = tk.Button(self.bframe, text="Go", width=7, relief=tk.SOLID,
            command=self.crypt, bg="#1e8931")
        self.bGo.pack(side=tk.RIGHT, padx=(5, 2), pady=(1, 1))
        self.bCA = tk.Button(self.bframe, text="Clear", width=6, 
            relief=tk.SOLID, command=self.clear_text, bg="#1e8931")
        self.bCA.pack(side=tk.RIGHT, pady=(1, 1))
        
        # key entry
        tk.Label(self.bframe, text="Key: ", width=3, anchor=tk.W,
		    bg="#1e8931").pack(side=tk.LEFT, padx=2, pady=(0, 1))
        self.eKy = tk.Entry(self.bframe, width=10, font="Helvetica 12 bold")
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
        text = self.text1.get(1.0, tk.END)[:-1]
        ct = Polyci()
        mtext = ""
        if key != "":
            if self.bEn["text"] == "Encrypt":
                mtext = ct.encrypt(text, key)
            else:
                mtext = ct.decrypt(text, key)
        else:
    	    mtext = "Insert key."
        self.text1.delete("1.0", tk.END)
        self.text1.insert(tk.END, mtext)
        
    
    def clear_text(self, *args):
        self.text1.delete("1.0", tk.END)
    
    
    def clear_entry(self, *args):
        self.eKy.delete("0", tk.END)
    
    
class Polyci:
    def decrypt(self, txt, key, *args):
        return self._modify_txt(txt, str(key), -1)
    
    
    def encrypt(self, txt, key, *args):
        return self._modify_txt(txt, str(key), 1)
    
    
    def _modify_txt(self, txt, key, mode):
	    # 0-255 ASCII some numbers missing, alternative needed
        self.code_book = [  # 189 letters and symbols
            "\t", " ", "!", "#", "$", "%", "&", "'", "(", ")",
            "*", "+", ",", "-", ".", "/", "0", "1", "2", "3",
            "4", "5", "6", "7", "8", "9", ":", ";", "<", "=",
            ">", "?", "@", "A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
            "]", "^", "_", "`", "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "{", "|", "}", "~", "¡", "¢", "£", "¤", "¥", "¦",
            "§", "¨", "©", "ª", "«", "¬", "®", "¯", "°", "±",
            "²", "³", "´", "µ", "¶", "·", "¸", "¹", "º", "»",
            "¼", "½", "¾", "¿", "À", "Á", "Â", "Ã", "Ä", "Å",
            "Æ", "Ç", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï",
            "Ð", "Ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "×", "Ø", "Ù",
            "Ú", "Û", "Ü", "Ý", "Þ", "ß", "à", "á", "â", "ã",
            "ä", "å", "æ", "ç", "è", "é", "ê", "ë", "ì", "í",
            "î", "ï", "ð", "ñ", "ò", "ó", "ô", "õ", "ö", "÷",
            "ø", "ù", "ú", "û", "ü", "ý", "þ", " ", "\n"
        ]
        txt, key, k_order = str(txt), str(key), 0
        modified_txt, cb = "", self.code_book
        for letter in txt:
            if key[k_order] not in cb:
                print("Error: Unknown key symbol.")
                return None
            if letter in cb:
                # Shift letter position based on key
                shift = cb.index(letter) + (cb.index(key[k_order]) * mode)
                shift = shift % len(cb)  # avoid overflow
                modified_txt += cb[shift]
            else:
                modified_txt += "?"  # unknown symbol
            k_order += 1
            if k_order >= len(key): k_order = 0
        return modified_txt
    
    
    def help(self):
        print("Functions:")
        for x in self.f.items():
            print("{} :: {}".format(x[0], x[1]))
        print()


def center(win, x_add=0, y_add=0):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x+x_add, y+y_add))
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PolyciUI(root)
    root.mainloop()		