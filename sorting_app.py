from tkinter import*
from tkinter import ttk,filedialog,messagebox
from tkinter import ttk
import os, shutil
class sorting_app:
    def __init__(self,root):
        self.root=root
        self.root.title("File Sorting Application | Developed by Tithi Debnath")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="File sorting application",font=("impact",40),bg="#808000",fg="white").place(x=0,y=0,relwidth=1)

        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select folder",font=("times new roman",25,"bold"),bg="white").place(x=50,y=100)
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=250,y=100,height=40,width=400)
        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE", font=("times new roman",15,"bold"),bg="#c0c0c0",fg="white",activebackground="#c0c0c0",activeforeground="white",cursor="hand2").place(x=700,y=95,height=45,width=150)
        hr=Label(self.root,bg="lightgray").place(x=50,y=160,height=2,widt=1250)



        self.image_extensions=["Image Extension",'.png','.jpg']
        self.audio_extensions=["Audio Extension",".mp3", ".amr"]
        self.video_extensions=["Video Extension",'.mp4','.avi','.mpeg4','.3gp']
        self.doc_extensions=["Document Extension",'.doc', '.xlsx', '.xls', '.pdf', '.zip','.pptx','.ppt']

        self.folders = {
                'videos': self.video_extensions,
                'audio': self.audio_extensions,
                'images': self.image_extensions,
                'documents': self.doc_extensions,
            }
    
        lbl_support_extension=Label(self.root,text="Various supported extensions",font=("times new roman",25,"bold"),bg="white").place(x=50,y=170)

        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.image_box.place(x=50,y=220,width=250,height=30)
        self.image_box.current(0)

        self.video_box=ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.video_box.place(x=390,y=220,width=250,height=30)
        self.video_box.current(0)

        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.audio_box.place(x=710,y=220,width=250,height=30)
        self.audio_box.current(0)

        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.doc_box.place(x=1030,y=220,width=250,height=30)
        self.doc_box.current(0)


        self.image_icon=PhotoImage(file="images/image_icon.png")
        self.video_icon=PhotoImage(file="images/video.png")
        self.audio_icon=PhotoImage(file="images/audio.png")
        self.doc_icon=PhotoImage(file="images/doc.png")
        self.other_icon=PhotoImage(file="images/others.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=300,width=1250,height=300)
       

        self.lbl_total_files=Label(Frame1,font=("times new roman",20,"bold"),bg="white")
        self.lbl_total_files.place(x=10,y=10)


        self.lbl_total_image=Label(Frame1, bd=2,relief=RAISED,image=self.image_icon,compound=TOP,font=("times new roman",20,"bold"),bg="yellow")
        self.lbl_total_image.place(x=30,y=50,width=200,height=230)

        self.lbl_total_video=Label(Frame1, bd=2,relief=RAISED,  image=self.video_icon,compound=TOP,font=("times new roman",20,"bold"),bg="yellow")
        self.lbl_total_video.place(x=270,y=50,width=200,height=230)

        self.lbl_total_audio=Label(Frame1, bd=2,relief=RAISED,  image=self.audio_icon,compound=TOP,font=("times new roman",20,"bold"),bg="yellow")
        self.lbl_total_audio.place(x=520,y=50,width=200,height=230)

        self.lbl_total_doc=Label(Frame1, bd=2,relief=RAISED,  image=self.doc_icon,compound=TOP,font=("times new roman",20,"bold"),bg="yellow")
        self.lbl_total_doc.place(x=770,y=50,width=200,height=230)

        self.lbl_total_other=Label(Frame1, bd=2,relief=RAISED, image=self.other_icon,compound=TOP,font=("times new roman",20,"bold"),bg="yellow")
        self.lbl_total_other.place(x=1020,y=50,width=200,height=230)

       
        lbl_status=Label(self.root,text="STATUS",font=("times new roman",25,"bold"),bg="white").place(x=50,y=620)
        self.lbl_st_total=Label(self.root,text="",font=("times new roman",18,"bold"),bg="white",fg="black")
        self.lbl_st_total.place(x=300,y=620)

        self.lbl_st_moved=Label(self.root,text="",font=("times new roman",18,"bold"),bg="white",fg="black")
        self.lbl_st_moved.place(x=500,y=620)

        self.lbl_st_left=Label(self.root,text="",font=("times new roman",18,"bold"),bg="white",fg="black")
        self.lbl_st_left.place(x=700,y=620)

        self.btn_clear=Button(self.root,text="CLEAR",command=self.clear,bd=4,relief=RAISED ,font=("times new roman",15,"bold"),bg="#c0c0c0",fg="white",activebackground="#c0c0c0",activeforeground="white",cursor="hand2")
        self.btn_clear.place(x=880,y=610,height=45,width=200)

        self.btn_start=Button(self.root,state=DISABLED,command=self.start_function,text="START",bd=4,relief=RAISED ,font=("times new roman",15,"bold"),bg="#c0c0c0",fg="white",activebackground="#c0c0c0",activeforeground="white",cursor="hand2")
        self.btn_start.place(x=1100,y=610,height=45,width=200)


    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        combine_list=[]

        for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i))==True:
                    self.count=self.count+1
                    ext ="."+i.split(".")[-1]
                    for folder_name in self.folders.items():
                        for x in folder_name[1]:
                            combine_list.append(x)
                        if ext.lower() in folder_name[1] and folder_name[0] == "images" :
                            images+=1
                        if ext.lower() in folder_name[1] and folder_name[0] == "audios" :
                            audios+=1
                        if ext.lower() in folder_name[1] and folder_name[0] == "videos" :
                            videos+=1
                        if ext.lower() in folder_name[1] and folder_name[0] == "documents" :
                            documents+=1
        for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i))==True:
                     ext ="."+i.split(".")[-1]
                     if ext.lower() not in combine_list:
                         others=others+1
                        
        self.lbl_total_image.config(text="Total images\n" + str(images))
        self.lbl_total_video.config(text="Total videos\n" + str(videos))
        self.lbl_total_audio.config(text="Total audios\n" + str(audios))
        self.lbl_total_doc.config(text="Total documents\n" + str(documents))
        self.lbl_total_other.config(text="Total other files\n" + str(others))
        self.lbl_total_files.config(text="Total files" + str(self.count))




    def browse_function(self):
            op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
            if op!=None:
                self.var_foldername.set(str(op))
                self.directory = self.var_foldername.get()
                self.other_name = "others"
                
                self.rename_folder()

                self.all_files = os.listdir(self.directory)

                length=len(self.all_files)
                count = 1
                self.Total_count()
                self.btn_start.config(state=NORMAL)
              
    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directory,i))==True:
                    c=c+1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL : " + str(self.count))
                    self.lbl_st_moved.config(text="MOVED : " + str(c))
                    self.lbl_st_left.config(text="LEFT : " + str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()
            messagebox.showinfo("success", "all files has moved successfully")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)

        else:
            messagebox.showerror("error"," please select right directory")
    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="" )
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")

        self.lbl_total_image.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_doc.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files")

    def rename_folder(self):
        for self.folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory,self.folder))==True:
                os.rename(os.path.join(self.directory,self.folder),os.path.join(self.directory,self.folder.lower()))

    def create_move(self,ext,file_name):
        find = False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory,folder_name))
                shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,folder_name))
                find=True
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory,self.other_name))
            shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,self.other_name))


       

      
root = Tk()
obj = sorting_app(root)
root.mainloop()
