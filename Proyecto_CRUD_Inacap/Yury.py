from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

# ==================================LOGIN============================================
def validar_usuario(usuario, contrasena):
    conexion = sqlite3.connect('Empleados.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleado WHERE nombre_completo=? AND contraseña=?", (usuario, contrasena))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado

def login():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    
    user_data = validar_usuario(usuario, contrasena)
    if user_data:
        tkMessageBox.showinfo("Login exitoso", "Bienvenido, {}".format(usuario))
        root_login.destroy()
        if user_data[1] == "RRHH":
            abrir_ventana_principal()
        else:
            abrir_ventana_empleado(user_data)
    else:
        tkMessageBox.showerror("Error de login", "Usuario o contraseña incorrectos")

root_login = Tk()
root_login.title("Login")

Label(root_login, text="Usuario").grid(row=0, column=0)
Label(root_login, text="Contraseña").grid(row=1, column=0)

usuario_entry = Entry(root_login)
contrasena_entry = Entry(root_login, show="*")

usuario_entry.grid(row=0, column=1)
contrasena_entry.grid(row=1, column=1)

Button(root_login, text="Login", command=login).grid(row=2, columnspan=2)

def abrir_ventana_principal():
    print("Abriendo ventana principal")  # Debug print
    root = Tk()
    root.title("Empleados")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.attributes("-fullscreen", True)

    def exit_fullscreen(event):
        root.attributes("-fullscreen", False)

    # ==================================METHODS============================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect('Empleados.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS `Empleado` (
                            Id_empleado INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            nombre_completo TEXT,
                            rut TEXT,
                            sexo TEXT,
                            direccion TEXT,
                            telefono TEXT,
                            cargo TEXT,
                            fecha_ingreso TEXT,
                            area TEXT,
                            contacto_emergencia_nombre TEXT,
                            contacto_emergencia_relacion TEXT,
                            contacto_emergencia_telefono TEXT,
                            carga_familiar_nombre TEXT,
                            carga_familiar_parentesco TEXT,
                            carga_familiar_sexo TEXT,
                            carga_familiar_rut TEXT,
                            contraseña TEXT)""")
        print("Base de datos inicializada")

    def Create():
        if NOMBRE_COMPLETO.get() == "" or RUT.get() == "" or SEXO.get() == "" or DIRECCION.get() == "" or TELEFONO.get() == "" or CARGO.get() == "" or FECHA_INGRESO.get() == "" or AREA.get() == "" or CONTACTO_NOMBRE.get() == "" or CONTACTO_RELACION.get() == "" or CONTACTO_TELEFONO.get() == "" or CARGA_NOMBRE.get() == "" or CARGA_PARENTESCO.get() == "" or CARGA_SEXO.get() == "" or CARGA_RUT.get() == "":
            txt_result.config(text="Por favor, ¡complete todos los campos!", fg="red")
        else:
            Database()
            cursor.execute("""INSERT INTO `Empleado` (nombre_completo, rut, sexo, direccion, telefono, cargo, fecha_ingreso, area, contacto_emergencia_nombre, contacto_emergencia_relacion, contacto_emergencia_telefono, carga_familiar_nombre, carga_familiar_parentesco, carga_familiar_sexo, carga_familiar_rut, contraseña) 
                            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (str(NOMBRE_COMPLETO.get()), str(RUT.get()), str(SEXO.get()), str(DIRECCION.get()), str(TELEFONO.get()), str(CARGO.get()), str(FECHA_INGRESO.get()), str(AREA.get()), str(CONTACTO_NOMBRE.get()), str(CONTACTO_RELACION.get()), str(CONTACTO_TELEFONO.get()), str(CARGA_NOMBRE.get()), str(CARGA_PARENTESCO.get()), str(CARGA_SEXO.get()), str(CARGA_RUT.get()), str(CONTRASEÑA.get())))
            tree.delete(*tree.get_children())
            cursor.execute("SELECT * FROM `Empleado` ORDER BY `nombre_completo` ASC")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16]))
            conn.commit()
            ClearFields()
            txt_result.config(text="¡Empleado creado!", fg="green")

    def Read():
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `Empleado` ORDER BY `nombre_completo` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16]))
        cursor.close()
        conn.close()
        txt_result.config(text="Información correctamente obtenida", fg="black")

    def Update():
        Database()
        if SEXO.get() == "":
            txt_result.config(text="Por favor selecciona un género", fg="red")
        else:
            tree.delete(*tree.get_children())
            cursor.execute("""UPDATE `Empleado` SET 
                                nombre_completo = ?, rut = ?, sexo =?, direccion = ?, telefono = ?, cargo = ?, fecha_ingreso = ?, area = ?, contacto_emergencia_nombre = ?, contacto_emergencia_relacion = ?, contacto_emergencia_telefono = ?, carga_familiar_nombre = ?, carga_familiar_parentesco = ?, carga_familiar_sexo = ?, carga_familiar_rut = ? 
                            WHERE `Id_empleado` = ?""", (str(NOMBRE_COMPLETO.get()), str(RUT.get()), str(SEXO.get()), str(DIRECCION.get()), str(TELEFONO.get()), str(CARGO.get()), str(FECHA_INGRESO.get()), str(AREA.get()), str(CONTACTO_NOMBRE.get()), str(CONTACTO_RELACION.get()), str(CONTACTO_TELEFONO.get()), str(CARGA_NOMBRE.get()), str(CARGA_PARENTESCO.get()), str(CARGA_SEXO.get()), str(CARGA_RUT.get()), int(Id_empleado)))
            conn.commit()
            cursor.execute("SELECT * FROM `Empleado` ORDER BY `nombre_completo` ASC")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16]))
            cursor.close()
            conn.close()
            ClearFields()
            btn_create.config(state=NORMAL)
            btn_read.config(state=NORMAL)
            btn_update.config(state=DISABLED)
            btn_delete.config(state=NORMAL)
            txt_result.config(text="Datos actualizados correctamente", fg="black")

    def OnSelected(event):
        global Id_empleado
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        Id_empleado = selecteditem[0]
        ClearFields()
        NOMBRE_COMPLETO.set(selecteditem[1])
        RUT.set(selecteditem[2])
        SEXO.set(selecteditem[3])
        DIRECCION.set(selecteditem[4])
        TELEFONO.set(selecteditem[5])
        CARGO.set(selecteditem[6])
        FECHA_INGRESO.set(selecteditem[7])
        AREA.set(selecteditem[8])
        CONTACTO_NOMBRE.set(selecteditem[9])
        CONTACTO_RELACION.set(selecteditem[10])
        CONTACTO_TELEFONO.set(selecteditem[11])
        CARGA_NOMBRE.set(selecteditem[12])
        CARGA_PARENTESCO.set(selecteditem[13])
        CARGA_SEXO.set(selecteditem[14])
        CARGA_RUT.set(selecteditem[15])
        CONTRASEÑA.set(selecteditem[16])

        btn_create.config(state=DISABLED)
        btn_read.config(state=DISABLED)
        btn_update.config(state=NORMAL)
        btn_delete.config(state=DISABLED)

    def Delete():
        if not tree.selection():
            txt_result.config(text="Por favor selecciona un empleado primero", fg="red")
        else:
            result = tkMessageBox.askquestion('Empleados', '¿Estás seguro de querer borrar esto?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                Database()
                cursor.execute("DELETE FROM `Empleado` WHERE `Id_empleado` = %d" % selecteditem[0])
                conn.commit()
                cursor.close()
                conn.close()
                txt_result.config(text="Datos borrados correctamente", fg="black")

    def Exit():
        result = tkMessageBox.askquestion('Empleados', '¿Seguro de que quieres salir?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    def ClearFields():
        NOMBRE_COMPLETO.set("")
        RUT.set("")
        SEXO.set("")
        DIRECCION.set("")
        TELEFONO.set("")
        CARGO.set("")
        FECHA_INGRESO.set("")
        AREA.set("")
        CONTACTO_NOMBRE.set("")
        CONTACTO_RELACION.set("")
        CONTACTO_TELEFONO.set("")
        CARGA_NOMBRE.set("")
        CARGA_PARENTESCO.set("")
        CARGA_SEXO.set("")
        CARGA_RUT.set("")

    # ==================================VARIABLES==========================================
    NOMBRE_COMPLETO = StringVar()
    RUT = StringVar()
    SEXO = StringVar()
    DIRECCION = StringVar()
    TELEFONO = StringVar()
    CARGO = StringVar()
    FECHA_INGRESO = StringVar()
    AREA = StringVar()
    CONTACTO_NOMBRE = StringVar()
    CONTACTO_RELACION = StringVar()
    CONTACTO_TELEFONO = StringVar()
    CARGA_NOMBRE = StringVar()
    CARGA_PARENTESCO = StringVar()
    CARGA_SEXO = StringVar()
    CARGA_RUT = StringVar()
    CONTRASEÑA = StringVar()

    # ==================================FRAME==============================================
    Top = Frame(root, width=900, height=50, bd=8, relief="raise")
    Top.pack(side=TOP, fill=X)

    Left = Frame(root, width=300, height=500, bd=8, relief="raise")
    Left.pack(side=LEFT, fill=BOTH, expand=True)

    entry_canvas = Canvas(Left)
    entry_scrollbar = Scrollbar(Left, orient="vertical", command=entry_canvas.yview)
    entry_frame = Frame(entry_canvas)

    entry_frame.bind(
        "<Configure>",
        lambda e: entry_canvas.configure(
            scrollregion=entry_canvas.bbox("all")
        )
    )

    entry_canvas.create_window((0, 0), window=entry_frame, anchor="nw")
    entry_canvas.configure(yscrollcommand=entry_scrollbar.set)

    entry_scrollbar.pack(side="right", fill="y")
    entry_canvas.pack(side="left", fill="both", expand=True)

    def on_mouse_wheel_left(event):
        if event.delta:
            entry_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            if event.num == 5:
                entry_canvas.yview_scroll(1, "units")
            elif event.num == 4:
                entry_canvas.yview_scroll(-1, "units")

    entry_canvas.bind_all("<MouseWheel>", on_mouse_wheel_left)
    entry_canvas.bind_all("<Button-4>", on_mouse_wheel_left)
    entry_canvas.bind_all("<Button-5>", on_mouse_wheel_left)

    Right = Frame(root, width=600, height=500, bd=8, relief="raise")
    Right.pack(side=RIGHT, fill=BOTH, expand=True)

    Forms = entry_frame
    Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
    Buttons.pack(side=BOTTOM)
    RadioGroup = Frame(Forms)
    Male = Radiobutton(RadioGroup, text="Masculino", variable=SEXO, value="Masculino", font=('arial', 16)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Femenino", variable=SEXO, value="Femenino", font=('arial', 16)).pack(side=LEFT)

    RadioGroup2 = Frame(Forms)
    Male = Radiobutton(RadioGroup2, text="Masculino", variable=CARGA_SEXO, value="Masculino", font=('arial', 16)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup2, text="Femenino", variable=CARGA_SEXO, value="Femenino", font=('arial', 16)).pack(side=LEFT)

    # ==================================LABEL WIDGET=======================================
    txt_title = Label(Top, width=900, font=('arial', 24), text="Empleados")
    txt_title.pack()
    txt_nombre_completo = Label(Forms, text="Nombre completo:", font=('arial', 16), bd=15)
    txt_nombre_completo.grid(row=0, sticky="e")
    txt_rut = Label(Forms, text="RUT:", font=('arial', 16), bd=15)
    txt_rut.grid(row=1, sticky="e")
    txt_sexo = Label(Forms, text="Sexo:", font=('arial', 16), bd=15)
    txt_sexo.grid(row=2, sticky="e")
    txt_direccion = Label(Forms, text="Dirección:", font=('arial', 16), bd=15)
    txt_direccion.grid(row=3, sticky="e")
    txt_telefono = Label(Forms, text="Teléfono:", font=('arial', 16), bd=15)
    txt_telefono.grid(row=4, sticky="e")
    txt_cargo = Label(Forms, text="Cargo:", font=('arial', 16), bd=15)
    txt_cargo.grid(row=5, sticky="e")
    txt_fecha_ingreso = Label(Forms, text="Fecha de ingreso:", font=('arial', 16), bd=15)
    txt_fecha_ingreso.grid(row=6, sticky="e")
    txt_area = Label(Forms, text="Área/Departamento:", font=('arial', 16), bd=15)
    txt_area.grid(row=7, sticky="e")
    txt_contacto_nombre = Label(Forms, text="Contacto emergencia (nombre):", font=('arial', 16), bd=15)
    txt_contacto_nombre.grid(row=8, sticky="e")
    txt_contacto_relacion = Label(Forms, text="Contacto emergencia (relación):", font=('arial', 16), bd=15)
    txt_contacto_relacion.grid(row=9, sticky="e")
    txt_contacto_telefono = Label(Forms, text="Contacto emergencia (teléfono):", font=('arial', 16), bd=15)
    txt_contacto_telefono.grid(row=10, sticky="e")
    txt_carga_nombre = Label(Forms, text="Carga familiar (nombre):", font=('arial', 16), bd=15)
    txt_carga_nombre.grid(row=11, sticky="e")
    txt_carga_parentesco = Label(Forms, text="Carga familiar (parentesco):", font=('arial', 16), bd=15)
    txt_carga_parentesco.grid(row=12, sticky="e")
    txt_carga_sexo = Label(Forms, text="Carga familiar (sexo):", font=('arial', 16), bd=15)
    txt_carga_sexo.grid(row=13, sticky="e")
    txt_carga_rut = Label(Forms, text="Carga familiar (RUT):", font=('arial', 16), bd=15)
    txt_carga_rut.grid(row=14, sticky="e")
    txt_contraseña = Label(Forms, text="Contraseña", font=('arial', 16), bd=15)
    txt_contraseña.grid(row=15, sticky="e")
    txt_result = Label(Buttons)
    txt_result.pack(side=TOP)

    # ==================================ENTRY WIDGET=======================================
    nombre_completo = Entry(Forms, textvariable=NOMBRE_COMPLETO, width=30)
    nombre_completo.grid(row=0, column=1)
    rut = Entry(Forms, textvariable=RUT, width=30)
    rut.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    direccion = Entry(Forms, textvariable=DIRECCION, width=30)
    direccion.grid(row=3, column=1)
    telefono = Entry(Forms, textvariable=TELEFONO, width=30)
    telefono.grid(row=4, column=1)
    cargo = Entry(Forms, textvariable=CARGO, width=30)
    cargo.grid(row=5, column=1)
    fecha_ingreso = Entry(Forms, textvariable=FECHA_INGRESO, width=30)
    fecha_ingreso.grid(row=6, column=1)
    area = Entry(Forms, textvariable=AREA, width=30)
    area.grid(row=7, column=1)
    contacto_nombre = Entry(Forms, textvariable=CONTACTO_NOMBRE, width=30)
    contacto_nombre.grid(row=8, column=1)
    contacto_relacion = Entry(Forms, textvariable=CONTACTO_RELACION, width=30)
    contacto_relacion.grid(row=9, column=1)
    contacto_telefono = Entry(Forms, textvariable=CONTACTO_TELEFONO, width=30)
    contacto_telefono.grid(row=10, column=1)
    carga_nombre = Entry(Forms, textvariable=CARGA_NOMBRE, width=30)
    carga_nombre.grid(row=11, column=1)
    carga_parentesco = Entry(Forms, textvariable=CARGA_PARENTESCO, width=30)
    carga_parentesco.grid(row=12, column=1)
    RadioGroup2.grid(row=13, column=1)
    carga_rut = Entry(Forms, textvariable=CARGA_RUT, width=30)
    carga_rut.grid(row=14, column=1)
    contraseña = Entry(Forms, textvariable=CONTRASEÑA, width=30, show="*")
    contraseña.grid(row=15, column=1)

    # ==================================BUTTONS WIDGET=====================================
    btn_create = Button(Buttons, width=20, text="Crear empleado", command=Create)
    btn_create.pack(side=TOP, pady=5)
    btn_read = Button(Buttons, width=20, text="Listar empleados", command=Read)
    btn_read.pack(side=TOP, pady=5)
    btn_update = Button(Buttons, width=20, text="Modificar empleado", command=Update, state=DISABLED)
    btn_update.pack(side=TOP, pady=5)
    btn_delete = Button(Buttons, width=20, text="Borrar empleado", command=Delete)
    btn_delete.pack(side=TOP, pady=5)
    btn_exit = Button(Buttons, width=20, text="Salir", command=Exit)
    btn_exit.pack(side=TOP, pady=5)

    # ==================================LIST WIDGET========================================
    scrollbary = Scrollbar(Right, orient=VERTICAL)
    scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
    tree = ttk.Treeview(Right, columns=("ID Empleado", "Nombre Completo", "RUT", "Sexo", "Cargo"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ID Empleado', text="ID Empleado", anchor=W)
    tree.heading('Nombre Completo', text="Nombre Completo", anchor=W)
    tree.heading('RUT', text="RUT", anchor=W)
    tree.heading('Sexo', text="Sexo", anchor=W)
    tree.heading('Cargo', text="Cargo", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=150)
    tree.pack()
    tree.bind('<Double-Button-1>', OnSelected)

    def on_mouse_wheel(event):
        if event.delta:
            tree.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            if event.num == 5:
                tree.yview_scroll(1, "units")
            elif event.num == 4:
                tree.yview_scroll(-1, "units")

    tree.bind_all("<MouseWheel>", on_mouse_wheel)
    tree.bind_all("<Button-4>", on_mouse_wheel)
    tree.bind_all("<Button-5>", on_mouse_wheel)

def abrir_ventana_empleado(user_data):
    root = Tk()
    root.title("Perfil de Empleado")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 600
    height = 400
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def Database():
        global conn, cursor
        conn = sqlite3.connect('Empleados.db')
        cursor = conn.cursor()
    
    def Update():
        Database()
        cursor.execute("""UPDATE Empleado SET 
                            nombre_completo = ?, sexo = ?, direccion = ?, telefono = ?, contacto_emergencia_nombre = ?, contacto_emergencia_relacion = ?, contacto_emergencia_telefono = ?, carga_familiar_nombre = ?, carga_familiar_parentesco = ?, carga_familiar_sexo = ?, carga_familiar_rut = ?, contraseña = ? 
                        WHERE Id_empleado = ?""", (str(NOMBRE_COMPLETO.get()), str(SEXO.get()), str(DIRECCION.get()), str(TELEFONO.get()), str(CONTACTO_NOMBRE.get()), str(CONTACTO_RELACION.get()), str(CONTACTO_TELEFONO.get()), str(CARGA_NOMBRE.get()), str(CARGA_PARENTESCO.get()), str(CARGA_SEXO.get()), str(CARGA_RUT.get()), str(CONTRASEÑA.get()), int(user_data[0])))
        conn.commit()
        cursor.close()
        conn.close()
        tkMessageBox.showinfo("Actualización exitosa", "Tus datos han sido actualizados correctamente")

    # Variables
    NOMBRE_COMPLETO = StringVar(value=user_data[1])
    CARGO = StringVar(value=user_data[4])
    SEXO = StringVar(value=user_data[3])
    DIRECCION = StringVar(value=user_data[4])
    TELEFONO = StringVar(value=user_data[5])
    CONTACTO_NOMBRE = StringVar(value=user_data[9])
    CONTACTO_RELACION = StringVar(value=user_data[10])
    CONTACTO_TELEFONO = StringVar(value=user_data[11])
    CARGA_NOMBRE = StringVar(value=user_data[12])
    CARGA_PARENTESCO = StringVar(value=user_data[13])
    CARGA_SEXO = StringVar(value=user_data[14])
    CARGA_RUT = StringVar(value=user_data[15])
    CONTRASEÑA = StringVar(value=user_data[16])

    # Frame
    form_frame = Frame(root, bd=8, relief="raise")
    form_frame.pack(side=TOP, fill=X)

    # Labels and Entries
    Label(form_frame, text="Nombre Completo:", font=('arial', 14)).grid(row=0, column=0, sticky="e")
    Entry(form_frame, textvariable=NOMBRE_COMPLETO, font=('arial', 14)).grid(row=0, column=1)

    Label(form_frame, text="Sexo:", font=('arial', 14)).grid(row=1, column=0, sticky="e")
    Entry(form_frame, textvariable=SEXO, font=('arial', 14)).grid(row=1, column=1)

    Label(form_frame, text="Dirección:", font=('arial', 14)).grid(row=2, column=0, sticky="e")
    Entry(form_frame, textvariable=DIRECCION, font=('arial', 14)).grid(row=2, column=1)

    Label(form_frame, text="Teléfono:", font=('arial', 14)).grid(row=3, column=0, sticky="e")
    Entry(form_frame, textvariable=TELEFONO, font=('arial', 14)).grid(row=3, column=1)

    Label(form_frame, text="Contacto de Emergencia (Nombre):", font=('arial', 14)).grid(row=4, column=0, sticky="e")
    Entry(form_frame, textvariable=CONTACTO_NOMBRE, font=('arial', 14)).grid(row=4, column=1)

    Label(form_frame, text="Contacto de Emergencia (Relación):", font=('arial', 14)).grid(row=5, column=0, sticky="e")
    Entry(form_frame, textvariable=CONTACTO_RELACION, font=('arial', 14)).grid(row=5, column=1)

    Label(form_frame, text="Contacto de Emergencia (Teléfono):", font=('arial', 14)).grid(row=6, column=0, sticky="e")
    Entry(form_frame, textvariable=CONTACTO_TELEFONO, font=('arial', 14)).grid(row=6, column=1)

    Label(form_frame, text="Carga Familiar (Nombre):", font=('arial', 14)).grid(row=7, column=0, sticky="e")
    Entry(form_frame, textvariable=CARGA_NOMBRE, font=('arial', 14)).grid(row=7, column=1)

    Label(form_frame, text="Carga Familiar (Parentesco):", font=('arial', 14)).grid(row=8, column=0, sticky="e")
    Entry(form_frame, textvariable=CARGA_PARENTESCO, font=('arial', 14)).grid(row=8, column=1)

    Label(form_frame, text="Carga Familiar (Sexo):", font=('arial', 14)).grid(row=9, column=0, sticky="e")
    Entry(form_frame, textvariable=CARGA_SEXO, font=('arial', 14)).grid(row=9, column=1)

    Label(form_frame, text="Carga Familiar (RUT):", font=('arial', 14)).grid(row=10, column=0, sticky="e")
    Entry(form_frame, textvariable=CARGA_RUT, font=('arial', 14)).grid(row=10, column=1)

    Label(form_frame, text="Contraseña:", font=('arial', 14)).grid(row=11, column=0, sticky="e")
    Entry(form_frame, textvariable=CONTRASEÑA, font=('arial', 14), show="*").grid(row=11, column=1)

    # Update Button
    Button(form_frame, text="Actualizar", font=('arial', 14), command=Update).grid(row=12, columnspan=2, pady=10)

# ==================================INITIALIZATION=====================================
if __name__ == '__main__':
    print("Ejecutando script...")
    root_login.mainloop()
