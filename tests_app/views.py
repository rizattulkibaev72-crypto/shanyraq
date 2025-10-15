from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Question

def tests_list(request):
    selected_theme = request.GET.get('theme')
    if selected_theme:
        tests = Test.objects.filter(theme=selected_theme)
    else:
        tests = Test.objects.all()

    themes = Test.THEMES
    return render(request, 'tests_app/tests_list.html', {
        'tests': tests,
        'themes': themes,
        'selected_theme': selected_theme,
    })

def test_detail(request, slug):
    test = get_object_or_404(Test, slug=slug)
    return render(request, 'tests_app/test_detail.html', {'test': test})

def test_start(request, slug):
    test = get_object_or_404(Test, slug=slug)
    questions = list(Question.objects.filter(test=test))
    total = len(questions)
    current = int(request.GET.get('q', 1))  # 👈 вот правильное имя переменной

    # Если пользователь прошёл все вопросы — показать результат
    if current > total:
        score = request.session.get(f'{test.slug}_score', 0)

        # Определяем уровень
        if score <= total * 1.5:
            result_text = "Низкий уровень эмоционального выгорания 🌿"
        elif score <= total * 2.3:
            result_text = "Средний уровень эмоционального выгорания 🌤"
        else:
            result_text = "Высокий уровень эмоционального выгорания 🔥"

        # Сохраняем результат
        from .models import TestResult
        TestResult.objects.create(
            user=request.user,
            test=test,
            score=score,
            result_text=result_text
        )

        # Очищаем сессию
        if f'{test.slug}_score' in request.session:
            del request.session[f'{test.slug}_score']

        return render(request, 'tests_app/test_result.html', {
            'test': test,
            'result_text': result_text,
        })

    question = questions[current - 1]

    if request.method == "POST":
        answer = request.POST.get('answer')
        score = request.session.get(f'{test.slug}_score', 0)

        if answer == "a":
            score += question.score_a
        elif answer == "b":
            score += question.score_b
        elif answer == "c":
            score += question.score_c

        request.session[f'{test.slug}_score'] = score
        # 👇 Исправлено: current вместо question_number
        return redirect(f'/tests/{test.slug}/start/?q={current + 1}')

    progress = int((current / total) * 100)

    return render(request, 'tests_app/test_start.html', {
        'test': test,
        'question': question,
        'current': current,
        'total': total,
        'progress': progress
    })
