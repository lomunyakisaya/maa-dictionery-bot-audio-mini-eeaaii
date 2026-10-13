from django.shortcuts import render

# Create your views here.
def home_view(request):
    if request.method == "POST":
        #BASIC LANGUAGE DATA
        word=request.POST.get("word").strip().lower()
        meaning=request.POST.get("meaning").strip().lower()
        context=request.POST.get("context").strip.lower()
        part_of_speech=request.POST.get("part_of_speech").strip().lower()

        #TRANSLATIONS
        english_translation=request.POST.get("english_translation").strip().lower()
        swahili_translation= request.POST.get("swahili_translation").strip().lower()

        #DIALET
        dialet= request.POST.get("dialet").strip().lower()
        region = request.POST.get("region").strip().lower()

        #AUDIO
        audio = request.POST.get("audio")

        #DATA SOURCE
        contributor_name = request.POST.get("contributor_name").strip().lower()
        source = request.POST.get("source").strip().lower()
        print(f"New Word {word} which means {meaning} given by {contributor_name}")

    return render(request, "maa/data.html")




