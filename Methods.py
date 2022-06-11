import Gui as g
import sys
import random
import tkinter.messagebox as mb


def main():
    g.Latte_Entry.insert("end", "0")
    g.Espresso_Entry.insert("end", "0")
    g.Iced_latte_Entry.insert("end", "0")
    g.SexOn_Entry.insert("end", "0")
    g.Cappucino_Entry.insert("end", "0")
    g.Frappé_Entry.insert("end", "0")
    g.Doppio_Entry.insert("end", "0")
    g.Iced_cap_Entry.insert("end", "0")
    g.Mojito_Entry.insert("end", "0")
    g.Cheese_Entry.insert("end", "0")
    g.Red_Entry.insert("end", "0")
    g.Pasta_Entry.insert("end", "0")
    g.lasagna_Entry.insert("end", "0")
    g.Carnitas_Entry.insert("end", "0")
    g.Cheeseburger_Entry.insert("end", "0")
    g.Layered_Entry.insert("end", "0")
    g.choc_Entry.insert("end", "0")
    g.Reuben_Entry.insert("end", "0")
    g.listbox_Drinks.insert("end", "0")
    g.listbox_Cakes.insert("end", "0")
    g.listbox_Charge.insert("end", "0")
    g.Tax_Listbox.insert("end", "0")
    g.Sub_Listbox.insert("end", "0")
    g.Total_Listbox.insert("end", "0")
    g.Cash_Entry.insert("end", "0")
    g.listbox_Remain.insert("end", "0")

    g.Latte_Entry.config(state="disabled")
    g.Reuben_Entry.config(state="disabled")
    g.choc_Entry.config(state="disabled")
    g.Layered_Entry.config(state="disabled")
    g.Cheeseburger_Entry.config(state="disabled")
    g.Carnitas_Entry.config(state="disabled")
    g.lasagna_Entry.config(state="disabled")
    g.Pasta_Entry.config(state="disabled")
    g.Red_Entry.config(state="disabled")
    g.Cheese_Entry.config(state="disabled")
    g.Mojito_Entry.config(state="disabled")
    g.Iced_cap_Entry.config(state="disabled")
    g.Doppio_Entry.config(state="disabled")
    g.Frappé_Entry.config(state="disabled")
    g.Cappucino_Entry.config(state="disabled")
    g.SexOn_Entry.config(state="disabled")
    g.Iced_latte_Entry.config(state="disabled")
    g.Espresso_Entry.config(state="disabled")

    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                           RESTAURANT BILLING SYSTEM")
    g.listbox.insert("end", "=================================================")

    g.window.mainloop()


def reset():
    m = mb.askyesno("SYSTEM ALERT", "Are You Sure Reset All..! \n")

    if m == 1:
        g.Latte_Entry.delete(0, 5)
        g.Espresso_Entry.delete(0, 5)
        g.Iced_latte_Entry.delete(0, 5)
        g.SexOn_Entry.delete(0, 5)
        g.Cappucino_Entry.delete(0, 5)
        g.Frappé_Entry.delete(0, 5)
        g.Doppio_Entry.delete(0, 5)
        g.Iced_cap_Entry.delete(0, 5)
        g.Mojito_Entry.delete(0, 5)
        g.Cheese_Entry.delete(0, 5)
        g.Red_Entry.delete(0, 5)
        g.Pasta_Entry.delete(0, 5)
        g.lasagna_Entry.delete(0, 5)
        g.Carnitas_Entry.delete(0, 5)
        g.Cheeseburger_Entry.delete(0, 5)
        g.Layered_Entry.delete(0, 5)
        g.choc_Entry.delete(0, 5)
        g.Reuben_Entry.delete(0, 5)
        g.listbox_Drinks.delete(0, 5)
        g.listbox_Cakes.delete(0, 5)
        g.listbox_Charge.delete(0, 5)
        g.Tax_Listbox.delete(0, 5)
        g.Sub_Listbox.delete(0, 5)
        g.Total_Listbox.delete(0, 5)
        g.Cash_Entry.delete(0, 5)
        g.listbox_Remain.delete(0, 5)
        g.Entry_Cal.delete(0, 10)

        g.Latte_Entry.insert("end", "0")
        g.Espresso_Entry.insert("end", "0")
        g.Iced_latte_Entry.insert("end", "0")
        g.SexOn_Entry.insert("end", "0")
        g.Cappucino_Entry.insert("end", "0")
        g.Frappé_Entry.insert("end", "0")
        g.Doppio_Entry.insert("end", "0")
        g.Iced_cap_Entry.insert("end", "0")
        g.Mojito_Entry.insert("end", "0")
        g.Cheese_Entry.insert("end", "0")
        g.Red_Entry.insert("end", "0")
        g.Pasta_Entry.insert("end", "0")
        g.lasagna_Entry.insert("end", "0")
        g.Carnitas_Entry.insert("end", "0")
        g.Cheeseburger_Entry.insert("end", "0")
        g.Layered_Entry.insert("end", "0")
        g.choc_Entry.insert("end", "0")
        g.Reuben_Entry.insert("end", "0")
        g.listbox_Drinks.insert("end", "0")
        g.listbox_Cakes.insert("end", "0")
        g.listbox_Charge.insert("end", "0")
        g.Tax_Listbox.insert("end", "0")
        g.Sub_Listbox.insert("end", "0")
        g.Total_Listbox.insert("end", "0")
        g.Cash_Entry.insert("end", "0")
        g.listbox_Remain.insert("end", "0")

        g.Latte_Entry.config(state="disabled")
        g.Reuben_Entry.config(state="disabled")
        g.choc_Entry.config(state="disabled")
        g.Layered_Entry.config(state="disabled")
        g.Cheeseburger_Entry.config(state="disabled")
        g.Carnitas_Entry.config(state="disabled")
        g.lasagna_Entry.config(state="disabled")
        g.Pasta_Entry.config(state="disabled")
        g.Red_Entry.config(state="disabled")
        g.Cheese_Entry.config(state="disabled")
        g.Mojito_Entry.config(state="disabled")
        g.Iced_cap_Entry.config(state="disabled")
        g.Doppio_Entry.config(state="disabled")
        g.Frappé_Entry.config(state="disabled")
        g.Cappucino_Entry.config(state="disabled")
        g.SexOn_Entry.config(state="disabled")
        g.Iced_latte_Entry.config(state="disabled")
        g.Espresso_Entry.config(state="disabled")

        g.var1.set(value=0)
        g.var2.set(value=0)
        g.var3.set(value=0)
        g.var4.set(value=0)
        g.var5.set(value=0)
        g.var6.set(value=0)
        g.var7.set(value=0)
        g.var8.set(value=0)
        g.var9.set(value=0)
        g.var10.set(value=0)
        g.var11.set(value=0)
        g.var12.set(value=0)
        g.var13.set(value=0)
        g.var14.set(value=0)
        g.var15.set(value=0)
        g.var16.set(value=0)
        g.var17.set(value=0)
        g.var18.set(value=0)

        g.listbox.delete(0, 20)
        g.listbox.insert("end", "=================================================")
        g.listbox.insert("end", "                                           RESTAURANT BILLING SYSTEM")
        g.listbox.insert("end", "=================================================")

    else:
        mb.showinfo("SYSTEM ALERT", "Canceled")


def total():
    l = int(g.Latte_Entry.get())
    e = int(g.Espresso_Entry.get())
    il = int(g.Iced_latte_Entry.get())
    v = int(g.SexOn_Entry.get())
    c = int(g.Cappucino_Entry.get())
    af = int(g.Frappé_Entry.get())
    am = int(g.Doppio_Entry.get())
    ic = int(g.Iced_cap_Entry.get())
    im = int(g.Mojito_Entry.get())
    sc = int(g.Cheese_Entry.get())
    su = int(g.Red_Entry.get())
    j = int(g.Pasta_Entry.get())
    w = int(g.lasagna_Entry.get())
    lc = int(g.Carnitas_Entry.get())
    k = int(g.Cheeseburger_Entry.get())
    ck = int(g.Layered_Entry.get())
    q = int(g.choc_Entry.get())
    p = int(g.Reuben_Entry.get())

    Latte, Espresso, Iced_latte, SexOn, Cappucino = 2, 1.69, 3, 2.30, 2
    Frappé, Doppio, Iced_cap, Mojito = 4, 3, 4, 1.50
    Cheese, Red, Pasta, lasagna, Carnitas = 2.95, 4, 9, 9.3, 6
    Cheeseburger, Layered, choc, Reuben = 3, 8, 6, 4.10

    tax, charge = 2.8, 1.0

    ll = Latte * l
    ee = Espresso * e
    ilil = Iced_latte * il
    vv = SexOn * v
    cc = Cappucino * c
    aaf = Frappé * af
    aam = Doppio * am
    icic = Iced_cap * ic
    imim = Mojito * im
    ssc = Cheese * sc
    ssu = Red * su
    jj = Pasta * j
    ww = lasagna * w
    llc = Carnitas * lc
    kk = Cheeseburger * k
    cck = Layered * ck
    qq = choc * q
    pp = Reuben * p

    drink = ll + ee + ilil + vv + cc + aaf + aam + icic + imim

    cake = ssc + ssu + jj + ww + llc + kk + cck + qq + pp

    if (drink + cake) == 0:
        tax = 0.0
        charge = 0.0

    sub = drink + cake + charge

    full_total = sub + tax

    g.listbox_Drinks.delete(0, 5)
    g.listbox_Cakes.delete(0, 5)
    g.listbox_Charge.delete(0, 5)
    g.Tax_Listbox.delete(0, 5)
    g.Sub_Listbox.delete(0, 5)
    g.Total_Listbox.delete(0, 5)

    g.listbox_Drinks.insert("end", "$ " + str('%.2f' % drink))
    g.listbox_Cakes.insert("end", "$ " + str('%.2f' % cake))
    g.listbox_Charge.insert("end", "$ " + str('%.2f' % charge))
    g.Tax_Listbox.insert("end", "$ " + str('%.2f' % tax))
    g.Sub_Listbox.insert("end", "$ " + str('%.2f' % sub))
    g.Total_Listbox.insert("end", "$ " + str('%.2f' % full_total))

    cash = int(g.Cash_Entry.get())
    remain = 0

    if cash != 0:
        remain = cash - full_total
        g.listbox_Remain.delete(0, 5)
        g.Entry_Cal.delete(0, 5)
        g.listbox_Remain.insert("end", "$ " + str('%.2f' % remain))

    return drink, cake, charge, tax, full_total, ll, ee, ilil, vv, cc, aaf, aam, icic, imim, ssc, ssu, jj, ww, llc, kk, cck, qq, pp, remain


def recipt():
    total_tuple = total()
    x = random.randint(1254, 3256)

    g.listbox.delete(0, 20)
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", ("Ref : " + str(x) + "                          RESTAURANT BILLING SYSTEM"))
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "           Items                             Number of Items                              Total")
    g.listbox.insert("end", "                                                 ")
    if g.var1.get() == 1: g.listbox.insert("end", "     Latte                                                {}                                            {}".format(g.Latte_Entry.get(), total_tuple[5]))
    if g.var2.get() == 1: g.listbox.insert("end", "     Espresso                                          {}                                            {}".format(g.Espresso_Entry.get(), total_tuple[6]))
    if g.var3.get() == 1: g.listbox.insert("end", "     Iced Latte                                         {}                                            {}".format(g.Iced_latte_Entry.get(), total_tuple[7]))
    if g.var4.get() == 1: g.listbox.insert("end", "     Sex On The Beach                           {}                                            {}".format(g.SexOn_Entry.get(), total_tuple[8]))
    if g.var5.get() == 1: g.listbox.insert("end", "     Cappuccino                                     {}                                            {}".format(g.Cappucino_Entry.get(), total_tuple[9]))
    if g.var6.get() == 1: g.listbox.insert("end", "     Frappé                                             {}                                            {}".format(g.Frappé_Entry.get(), total_tuple[10]))
    if g.var7.get() == 1: g.listbox.insert("end", "     Doppio                                            {}                                            {}".format(g.Doppio_Entry.get(), total_tuple[11]))
    if g.var8.get() == 1: g.listbox.insert("end", "     Iced Cappuccino                             {}                                            {}".format(g.Iced_cap_Entry.get(), total_tuple[12]))
    if g.var9.get() == 1: g.listbox.insert("end", "     Mojito                                              {}                                            {}".format(g.Mojito_Entry.get(), total_tuple[13]))
    if g.var10.get() == 1: g.listbox.insert("end", "     Cheese Cake                                     {}                                           {}".format(g.Cheese_Entry.get(), total_tuple[14]))
    if g.var11.get() == 1: g.listbox.insert("end", "     Red Velvet Cake                                {}                                          {}".format(g.Red_Entry.get(), total_tuple[15]))
    if g.var12.get() == 1: g.listbox.insert("end", "     Pasta Puttanesca                              {}                                          {}".format(g.Pasta_Entry.get(), total_tuple[16]))
    if g.var13.get() == 1: g.listbox.insert("end", "     Lasagna Bolognese                          {}                                          {}".format(g.lasagna_Entry.get(), total_tuple[17]))
    if g.var14.get() == 1: g.listbox.insert("end", "     Carnitas Burrito                                {}                                          {}".format(g.Carnitas_Entry.get(), total_tuple[18]))
    if g.var15.get() == 1: g.listbox.insert("end", "     Cheeseburger                                   {}                                          {}".format(g.Cheeseburger_Entry.get(), total_tuple[19]))
    if g.var16.get() == 1: g.listbox.insert("end", "     Layered Rainbow Cake                     {}                                          {}".format(g.Layered_Entry.get(), total_tuple[20]))
    if g.var17.get() == 1: g.listbox.insert("end", "     Choc-Honeycomb Cake                    {}                                          {}".format(g.choc_Entry.get(), total_tuple[21]))
    if g.var18.get() == 1: g.listbox.insert("end", "     Reuben Sandwich                            {}                                          {}".format(g.Reuben_Entry.get(), total_tuple[22]))

    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", ("     Cost of Drinks : " + "                                                                            $ " + str('%.2f' % total_tuple[0])))
    g.listbox.insert("end", ("     Cost of Food Items : " + "                                                                    $ " + str('%.2f' % total_tuple[1])))
    g.listbox.insert("end", ("     Service Charge : " + "                                                                           $ " + str('%.2f' % total_tuple[2])))
    g.listbox.insert("end", ("     Paid Tax : " + "                                                                                      $ " + str('%.2f' % total_tuple[3])))
    g.listbox.insert("end", ("     Total : " + "                                                                                           $ " + str('%.2f' % total_tuple[4])))
    if float(g.Cash_Entry.get()) != 0: g.listbox.insert("end", "     Cash                                                                                               $ {}".format('%.2f' % float(g.Cash_Entry.get())))
    if float(g.Cash_Entry.get()) != 0: g.listbox.insert("end", "     Remain                                                                                           $ {}".format('%.2f' % float(total_tuple[23])))

    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "=================================================")


def exit_window():
    m = mb.askyesno("SYSTEM ALERT", "Are You Sure Exit From System \n")
    if m == 1:
        sys.exit()

    else:
        mb.showinfo("SYSTEM ALERT", "Canceled")


calculator = ""


def set_number7():
    global calculator
    calculator = calculator + "7"
    g.Entry_Cal.insert("end", "7")


def set_number8():
    global calculator
    calculator = calculator + "8"
    g.Entry_Cal.insert("end", "8")


def set_number9():
    global calculator
    calculator = calculator + "9"
    g.Entry_Cal.insert("end", "9")


def set_number6():
    global calculator
    calculator = calculator + "6"
    g.Entry_Cal.insert("end", "6")


def set_number5():
    global calculator
    calculator = calculator + "5"
    g.Entry_Cal.insert("end", "5")


def set_number4():
    global calculator
    calculator = calculator + "4"
    g.Entry_Cal.insert("end", "4")


def set_number3():
    global calculator
    calculator = calculator + "3"
    g.Entry_Cal.insert("end", "3")


def set_number2():
    global calculator
    calculator = calculator + "2"
    g.Entry_Cal.insert("end", "2")


def set_number1():
    global calculator
    calculator = calculator + "1"
    g.Entry_Cal.insert("end", "1")


def set_number0():
    global calculator
    calculator = calculator + "0"
    g.Entry_Cal.insert("end", "0")


def set_number_plus():
    global calculator
    calculator = calculator + " + "
    g.Entry_Cal.insert("end", " + ")


def set_number_minus():
    global calculator
    calculator = calculator + " - "
    g.Entry_Cal.insert("end", " - ")


def set_number_div():
    global calculator
    calculator = calculator + " / "
    g.Entry_Cal.insert("end", " / ")


def set_number_sub():
    global calculator
    calculator = calculator + " * "
    g.Entry_Cal.insert("end", " * ")


def set_number_dot():
    global calculator
    calculator = calculator + "."
    g.Entry_Cal.insert("end", ".")


def equal():
    g.Entry_Cal.delete(0, 50)
    global calculator
    g.Entry_Cal.insert("end", eval(calculator))


def clear():
    global calculator
    calculator = ""
    g.Entry_Cal.delete(0, 50)


def Latte():
    if g.var1.get() == 1:
        g.Latte_Entry.config(state="normal")
        g.Latte_Entry.delete(0, 5)
    else:
        g.Latte_Entry.delete(0, 5)
        g.Latte_Entry.insert("end", "0")
        g.Latte_Entry.config(state="disabled")


def Espresso():
    if g.var2.get() == 1:
        g.Espresso_Entry.config(state="normal")
        g.Espresso_Entry.delete(0, 5)
    else:
        g.Espresso_Entry.delete(0, 5)
        g.Espresso_Entry.insert("end", "0")
        g.Espresso_Entry.config(state="disabled")


def Iced_latte():
    if g.var3.get() == 1:
        g.Iced_latte_Entry.config(state="normal")
        g.Iced_latte_Entry.delete(0, 5)
    else:
        g.Iced_latte_Entry.delete(0, 5)
        g.Iced_latte_Entry.insert("end", "0")
        g.Iced_latte_Entry.config(state="disabled")


def SexOn():
    if g.var4.get() == 1:
        g.SexOn_Entry.config(state="normal")
        g.SexOn_Entry.delete(0, 5)
    else:
        g.SexOn_Entry.delete(0, 5)
        g.SexOn_Entry.insert("end", "0")
        g.SexOn_Entry.config(state="disabled")


def Cappucino():
    if g.var5.get() == 1:
        g.Cappucino_Entry.config(state="normal")
        g.Cappucino_Entry.delete(0, 5)
    else:
        g.Cappucino_Entry.delete(0, 5)
        g.Cappucino_Entry.insert("end", "0")
        g.Cappucino_Entry.config(state="disabled")


def Frappé():
    if g.var6.get() == 1:
        g.Frappé_Entry.config(state="normal")
        g.Frappé_Entry.delete(0, 5)
    else:
        g.Frappé_Entry.delete(0, 5)
        g.Frappé_Entry.insert("end", "0")
        g.Frappé_Entry.config(state="disabled")


def Doppio():
    if g.var7.get() == 1:
        g.Doppio_Entry.config(state="normal")
        g.Doppio_Entry.delete(0, 5)
    else:
        g.Doppio_Entry.delete(0, 5)
        g.Doppio_Entry.insert("end", "0")
        g.Doppio_Entry.config(state="disabled")


def Iced_cap():
    if g.var8.get() == 1:
        g.Iced_cap_Entry.config(state="normal")
        g.Iced_cap_Entry.delete(0, 5)
    else:
        g.Iced_cap_Entry.delete(0, 5)
        g.Iced_cap_Entry.insert("end", "0")
        g.Iced_cap_Entry.config(state="disabled")


def Mojito():
    if g.var9.get() == 1:
        g.Mojito_Entry.config(state="normal")
        g.Mojito_Entry.delete(0, 5)
    else:
        g.Mojito_Entry.delete(0, 5)
        g.Mojito_Entry.insert("end", "0")
        g.Mojito_Entry.config(state="disabled")


def Cheese():
    if g.var10.get() == 1:
        g.Cheese_Entry.config(state="normal")
        g.Cheese_Entry.delete(0, 5)
    else:
        g.Cheese_Entry.delete(0, 5)
        g.Cheese_Entry.insert("end", "0")
        g.Cheese_Entry.config(state="disabled")


def Red():
    if g.var11.get() == 1:
        g.Red_Entry.config(state="normal")
        g.Red_Entry.delete(0, 5)
    else:
        g.Red_Entry.delete(0, 5)
        g.Red_Entry.insert("end", "0")
        g.Red_Entry.config(state="disabled")


def Pasta():
    if g.var12.get() == 1:
        g.Pasta_Entry.config(state="normal")
        g.Pasta_Entry.delete(0, 5)
    else:
        g.Pasta_Entry.delete(0, 5)
        g.Pasta_Entry.insert("end", "0")
        g.Pasta_Entry.config(state="disabled")


def lasagna():
    if g.var13.get() == 1:
        g.lasagna_Entry.config(state="normal")
        g.lasagna_Entry.delete(0, 5)
    else:
        g.lasagna_Entry.delete(0, 5)
        g.lasagna_Entry.insert("end", "0")
        g.lasagna_Entry.config(state="disabled")


def Carnitas():
    if g.var14.get() == 1:
        g.Carnitas_Entry.config(state="normal")
        g.Carnitas_Entry.delete(0, 5)
    else:
        g.Carnitas_Entry.delete(0, 5)
        g.Carnitas_Entry.insert("end", "0")
        g.Carnitas_Entry.config(state="disabled")


def Cheeseburger():
    if g.var15.get() == 1:
        g.Cheeseburger_Entry.config(state="normal")
        g.Cheeseburger_Entry.delete(0, 5)
    else:
        g.Cheeseburger_Entry.delete(0, 5)
        g.Cheeseburger_Entry.insert("end", "0")
        g.Cheeseburger_Entry.config(state="disabled")


def Layered():
    if g.var16.get() == 1:
        g.Layered_Entry.config(state="normal")
        g.Layered_Entry.delete(0, 5)
    else:
        g.Layered_Entry.delete(0, 5)
        g.Layered_Entry.insert("end", "0")
        g.Layered_Entry.config(state="disabled")


def choc():
    if g.var17.get() == 1:
        g.choc_Entry.config(state="normal")
        g.choc_Entry.delete(0, 5)
    else:
        g.choc_Entry.delete(0, 5)
        g.choc_Entry.insert("end", "0")
        g.choc_Entry.config(state="disabled")


def Reuben():
    if g.var18.get() == 1:
        g.Reuben_Entry.config(state="normal")
        g.Reuben_Entry.delete(0, 5)
    else:
        g.Reuben_Entry.delete(0, 5)
        g.Reuben_Entry.insert("end", "0")
        g.Reuben_Entry.config(state="disabled")


if __name__ == '__main__':
    main()
