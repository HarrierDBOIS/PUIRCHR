function redirectToPage(button) {
    window.location.href = button.id + '.html';
}

document.addEventListener("DOMContentLoaded", function () {
    const submitBtn = document.getElementById('submit-btn');
    let answers = {}; // Словарь для хранения ответов

    submitBtn.addEventListener('click', function (event) {
        event.preventDefault(); // Предотвращаем стандартное поведение формы

        // Получаем номер текущего вопроса (это можно сделать динамически)
        const currentQuestionNumber = 1; // Для примера, можно динамически менять этот номер

        // Получаем выбранный ответ (когда пользователь выбирает радио-кнопку)
        const selectedAnswer = document.querySelector('input[name="answer"]:checked');
        if (selectedAnswer) {
            // Сохраняем выбранный ответ в словарь
            answers[currentQuestionNumber] = selectedAnswer.value;
            console.log(answers); // Выводим ответы в консоль для проверки

            // Перенаправляем пользователя на следующий вопрос
            // (в данном примере просто обновляем страницу, можно настроить на динамическое обновление)
            setTimeout(function () {
                window.location.href = `question${currentQuestionNumber + 1}.html`; // Переход на следующий вопрос
            }, 1000); // Задержка в 1 секунду для пользователя, чтобы увидеть сохранение
        } else {
            alert("Пожалуйста, выберите ответ!");
        }
    });
});
