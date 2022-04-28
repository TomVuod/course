from django import forms

class ExerciseForm_1(forms.Form):
    mean_x=forms.DecimalField(label="średnia wartość x",required=False,
                              decimal_places=3)
    mean_y=forms.DecimalField(label="średnia wartość y",required=False,
                              decimal_places=3)
    sd_y=forms.DecimalField(label="odchylenie standardowe y",required=False,
                            decimal_places=3)
    condition_counter=forms.IntegerField(label="liczba wartości y większych od średniej powięszkonej o odchylenie standardowe",
                               required=False)
    correlation=forms.DecimalField(label="wartość wpółczynnika korelacji",
                           required=False,decimal_places=3)
    a=forms.DecimalField(label="wartość współczynnika nachylenia prostej",
                         required=False,decimal_places=3)
    b=forms.DecimalField(label="wartość wyrazu wolnego",required=False,
                         decimal_places=3)

class ExerciseForm_2(forms.Form):
    mean_residual=forms.DecimalField(label="średnia reszta (odchylenie)",
                                  required=False,decimal_places=3)
    sd_residual=forms.DecimalField(label="odchylenie standardowe reszt",
                                required=False,decimal_places=3)
    max_dev_x=forms.DecimalField(label="wartość x, dla której odchylenie jest największe",
                                   required=False,decimal_places=3)
    tss=forms.DecimalField(label="suma kwadratów odchyleń",required=False,
                           decimal_places=3)
    cumsum_resid_30=forms.DecimalField(label="elemnt nr 30 skumulowanych sum reszt",
    required=False, decimal_places=3)



class ExerciseForm_3(forms.Form):
    angle=forms.DecimalField(label="Kąt prostej regresji z osią odciętych",
    required=False, decimal_places=3)
    min_y_prim=forms.DecimalField(label="Wartość minimalna y'", required=False,
                                  decimal_places=3)
    correlation_prim=forms.DecimalField(label="Współczynnik korelacji po rotacji",
    required=False, decimal_places=3)
    a_prim=forms.DecimalField(label="Współczynnik kierunkowy po rotacji", required=False,
                                  decimal_places=3)
    b_prim=forms.DecimalField(label="Wyraz wolny po rotacji", required=False,
                                  decimal_places=3)
