from django.shortcuts import render, redirect
from app.forms import livroForm, emprestimoForm
from app.models import livro, emprestimo
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def home(request):
    data = {}
    search = request.GET.get("search")
    buscar_data = request.GET.get("buscar_data")
    filter = request.GET.get("filter_livro")
    filterAlf = request.GET.get("filterAlf_livro")
    if search:
        data["db"] = livro.objects.filter(nome__icontains=search)
        paginator = Paginator(data['db'], 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)

    elif filter:
        data["db"] = livro.objects.filter(tipo__icontains=filter).order_by('-criado_em')
        paginator = Paginator(data['db'], 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)

    elif filterAlf:

        if filterAlf == 'crescente':
            data["db"] = livro.objects.all().order_by('nome', '-criado_em')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

        elif filterAlf == 'recentes':
            data["db"] = livro.objects.all().order_by('-data', '-criado_em')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

        elif filterAlf == 'antigos':
            data["db"] = livro.objects.all().order_by('data', '-criado_em')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

        else:
            data["db"] = livro.objects.all().order_by('-nome', '-criado_em')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

    elif buscar_data:
        data["db"] = livro.objects.filter(data__icontains=buscar_data)
        paginator = Paginator(data['db'], 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)
    else:
        data["db"] = livro.objects.all().order_by('-criado_em')

        livro_list = livro.objects.all().order_by('-criado_em')
        paginator = Paginator(livro_list, 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)
        # all = livro.objects.all()
        # paginator = Paginator(all, 2)
        # pages = request.GET.get('page')
        # data['db'] = paginator.get_page(pages)
        # data['db'] = livro.objects.all()
    return render(request, "index.html", data)


@login_required()
def form(request):
    data = {}
    data["form"] = livroForm()
    return render(request, "form.html", data)


@login_required()
def create(request):
    form = livroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")


@login_required()
def view(request, pk):
    data = {}
    data["db"] = livro.objects.get(pk=pk)
    return render(request, "view.html", data)


@login_required()
def edit(request, pk):
    data = {}
    data["db"] = livro.objects.get(pk=pk)
    data["form"] = livroForm(instance=data["db"])
    return render(request, "form.html", data)


@login_required()
def update(request, pk):
    data = {}
    data["db"] = livro.objects.get(pk=pk)
    form = livroForm(request.POST or None, instance=data["db"])
    if form.is_valid():
        form.save()
        return redirect("home")


@login_required()
def delete(request, pk):
    db = livro.objects.get(pk=pk)
    db.delete()
    return redirect("home")


@login_required()
def table(request):
    data = {}
    etiqueta = request.GET.get("etiqueta")
    if etiqueta:
        if etiqueta == 'etiqueta':
            data['table'] = livro.objects.all()
        else:
            data['db'] = livro.objects.all()  # livroForm()
    else:
        data['db'] = livro.objects.all()
    return render(request, "table.html", data)


@login_required()
def homeem(request): #nao precisa mais dele
    data = {}
    searchem = request.GET.get("searchem")
    if searchem:
        data["db"] = emprestimo.objects.filter(pessoa__icontains=searchem)
        paginator = Paginator(data['db'], 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)

    else:
        data["db"] = emprestimo.objects.all()

        emprestimo_list = livro.objects.all()
        paginator = Paginator(emprestimo_list, 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)
    return render(request, "emprestimo.html", data)


@login_required()
def list_emprestimo(request):
    data = {}
    #data["db"] = emprestimo.objects.all()
    searchem = request.GET.get("searchem")
    buscar_data = request.GET.get("buscar_data_emp")
    filter = request.GET.get("filter")
    filterAlf = request.GET.get("filterAlf")

    if searchem:
        data["db"] = emprestimo.objects.filter(pessoa__icontains=searchem)
        paginator = Paginator(data['db'], 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)

    elif filter:

        data["db"] = emprestimo.objects.filter(estado__icontains=filter).order_by('-criado_emp')
        paginator = Paginator(data['db'], 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)

    elif filterAlf:

        if filterAlf == 'crescente':
            data["db"] = emprestimo.objects.all().order_by('pessoa')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

        elif filterAlf == 'recentes':
            data["db"] = emprestimo.objects.all().order_by('-criado_emp')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

        elif filterAlf == 'antigos':
            data["db"] = emprestimo.objects.all().order_by('criado_emp')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

        elif filterAlf == 'serie':
            data["db"] = emprestimo.objects.all().order_by('serie')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

        else:
            data["db"] = emprestimo.objects.all().order_by('-pessoa')
            paginator = Paginator(data['db'], 10)
            page = request.GET.get('page')
            data['db'] = paginator.get_page(page)

    elif buscar_data:
        data['db'] = emprestimo.objects.filter(dataem__icontains=buscar_data)
        paginator = Paginator(data['db'], 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)

    else:
        data["db"] = emprestimo.objects.all().order_by('-estado', '-criado_emp')

        emprestimo_list = emprestimo.objects.all().order_by('-estado', '-criado_emp')
        paginator = Paginator(emprestimo_list, 10)
        page = request.GET.get('page')
        data['db'] = paginator.get_page(page)
    return render(request, "emprestimo.html", data)


@login_required()
def createem(request):
    if request.POST:
        option = request.POST["states[]"]
        dataem = request.POST["data"]
        pessoa = request.POST["dest"]
        quantidadeem = request.POST["quant"]
        estado = request.POST["estado"]
        serie = request.POST["serie"]
        emprestimo_feito = emprestimo.objects.create(
            nome_id=option, dataem=dataem, pessoa=pessoa, quantidadeem=quantidadeem, estado=estado, serie=serie
        )
        emprestimo_feito.save()
        return redirect("emprestimo")
    data = {}
    data["db"] = livro.objects.all()
    return render(request, "formem.html", data)


@login_required()
def viewem(request, pk):
    data = {}
    data["db"] = get_object_or_404(emprestimo, pk=pk)
    return render(request, "viewem.html", data)


@login_required()
def editem(request, pk):            #puxa o formulário vindo do batão editar do emprestimo.html
    data = {}
    if request.POST:
        data["db"] = emprestimo.objects.get(pk=pk)
        print(data['db'])
    return render(request, "formem.html", data)


@login_required()
def editemp(request, pk):
    data = {}
    data['db'] = livro.objects.all()
    data['pk'] = pk
    data['emprestimo'] = emprestimo.objects.get(id=pk)
    if request.POST:
        registro = emprestimo.objects.get(pk=pk)
        option = request.POST["states[]"]
        dataem = request.POST["data"]
        pessoa = request.POST["dest"]
        quantidadeem = request.POST["quant"]
        serie = request.POST["serie"]
        estado = request.POST["estado"]
        registro.nome_id = option
        #lista = map(int, request.POST.getlist("states[]"))
        #lista = request.POST.getlist("states[]")
        #print(lista)
        registro.dataem = dataem
        registro.pessoa = pessoa
        registro.quantidadeem = quantidadeem
        registro.serie = serie
        registro.estado = estado
        registro.save()
        return redirect('emprestimo')   #(request, 'emprestimo.html', data)
    return render(request, 'editemp.html', data) #editemp.html



@login_required()
def updateem(request, pk):  #faz o update no banco
    data = {}
    data["db"] = emprestimo.objects.get(pk=pk)
    form = emprestimoForm(request.POST or None, instance=data["db"])
    if form.is_valid():
        form.save()
        return redirect("emprestimo")


@login_required()
def deleteem(request, pk):
    db = emprestimo.objects.get(pk=pk)
    db.delete()
    return redirect("emprestimo")


@login_required()
def tableem(request):
    data = {}
    data["db"] = data["db"] = emprestimo.objects.all().order_by('-estado', 'serie')  # livroForm()
    return render(request, "tableem.html", data)


@login_required()
def changeStatus(request, pk):
    data = {}
    data["db"] = emprestimo.objects.get(pk=pk)

    if(data['db'].estado == 'emprestado'):
        data['db'].estado = 'devolvido'
    else:
        data['db'].estado = 'emprestado'
    data['db'].save()
    return redirect("emprestimo")

