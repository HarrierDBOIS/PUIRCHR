document.addEventListener('DOMContentLoaded', function () {
  // Получаем данные из тега <script>
  const quizDataElement = document.getElementById('quiz-data');
  const quizData = JSON.parse(quizDataElement.textContent);
  const testName = quizData.name;          // Имя теста
  const questions = quizData.questions;      // Массив вопросов

  let currentQuestionIndex = 0;
  const selectedAnswers = []; // Массив для хранения выбранных ответов

  const questionText = document.getElementById('question-text');
  const answerA = document.getElementById('answer_A');
  const answerB = document.getElementById('answer_B');
  const answerC = document.getElementById('answer_C');
  const answerD = document.getElementById('answer_D');

  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const finishBtn = document.getElementById('finish-btn');
  const questionButtons = document.querySelectorAll('.question-btn');

  // Функция для обновления отображения вопроса
  function updateQuestion(index) {
    const question = questions[index];
    questionText.textContent = question.question;
    answerA.nextElementSibling.textContent = question.answer_A;
    answerB.nextElementSibling.textContent = question.answer_B;

    if (question.answer_C) {
      answerC.parentElement.style.display = 'block';
      answerC.nextElementSibling.textContent = question.answer_C;
    }


    // Снимаем отметку с выбранных радио-кнопок
    document.querySelectorAll('input[name="answer"]').forEach(radio => radio.checked = false);

    // Обновляем состояние кнопок навигации
    prevBtn.disabled = index === 0;
    nextBtn.style.display = index === questions.length - 1 ? 'none' : 'inline-block';
    finishBtn.style.display = index === questions.length - 1 ? 'inline-block' : 'none';

    // Обновляем внешний вид кнопок навигации
    questionButtons.forEach((btn, i) => {
      btn.classList.toggle('active', i === index);
      btn.classList.toggle('answered', !!selectedAnswers[i]);
    });

    // Если для текущего вопроса уже был выбран ответ, отмечаем его
    if (selectedAnswers[index]) {
      const savedAnswerKey = selectedAnswers[index]; // Сохранённое значение (например, "answer_A")
      const selectedRadio = document.querySelector(`input[name="answer"][value="${savedAnswerKey}"]`);
      if (selectedRadio) {
        selectedRadio.checked = true;
      }
    }

    // Проверяем, можно ли завершить тест
    checkFinishButtonState();
  }

  // Функция для проверки, заполнены ли все ответы
  function checkFinishButtonState() {
    const allAnswered = selectedAnswers.length === questions.length &&
      selectedAnswers.every(answer => answer !== undefined);
    finishBtn.disabled = !allAnswered;
  }

  // Обработчик кнопки "Предыдущий"
  prevBtn.addEventListener('click', () => {
    if (currentQuestionIndex > 0) {
      currentQuestionIndex--;
      updateQuestion(currentQuestionIndex);
    }
  });

  // Обработчик кнопки "Следующий"
  nextBtn.addEventListener('click', () => {
    const selectedRadio = document.querySelector('input[name="answer"]:checked');
    if (!selectedRadio) {
      alert('Пожалуйста, выберите ответ.');
      return;
    }

    // Сохраняем выбранный ответ для текущего вопроса
    const selectedAnswerKey = selectedRadio.value; // Например, "answer_A"
    selectedAnswers[currentQuestionIndex] = selectedAnswerKey;

    if (currentQuestionIndex < questions.length - 1) {
      currentQuestionIndex++;
      updateQuestion(currentQuestionIndex);
    } else {
      checkFinishButtonState();
    }
  });
  // Обработчик изменения состояния радио-кнопок
  document.querySelectorAll('input[name="answer"]').forEach(radio => {
    radio.addEventListener('change', () => {
      // Сохраняем выбранный ответ для текущего вопроса
      const selectedAnswerKey = document.querySelector('input[name="answer"]:checked').value;
      selectedAnswers[currentQuestionIndex] = selectedAnswerKey;

      // Проверяем состояние кнопки "Закончить"
      checkFinishButtonState();
    });
  });

  // Обработчик кнопки "Закончить"
finishBtn.addEventListener('click', () => {
    const selectedRadio = document.querySelector('input[name="answer"]:checked');
    if (!selectedRadio) {
      alert('Пожалуйста, выберите ответ.');
      return;
    }
    // Сохраняем выбранный ответ для последнего вопроса
    const selectedAnswerKey = selectedRadio.value; // Например, "answer_A"
    selectedAnswers[currentQuestionIndex] = selectedAnswerKey;
    checkFinishButtonState();
    // Отправляем POST-запрос с результатами
    fetch(`/api/main/test/result/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ test_name: testName, answers: selectedAnswers })
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Ошибка при отправке данных');
        }
        return response.text(); // Получаем HTML-ответ
      })
      .then(html => {
        // Заменяем содержимое текущей страницы на полученный HTML
        document.open();
        document.write(html);
        document.close();
      })
      .catch((error) => {
        console.error('Error:', error);
      });
});
  // Обработчик клика по кнопкам навигации вопросов
  questionButtons.forEach((btn, index) => {
    btn.addEventListener('click', () => {
      const selectedRadio = document.querySelector('input[name="answer"]:checked');
      if (selectedRadio) {
        const selectedAnswerKey = selectedRadio.value;
        selectedAnswers[currentQuestionIndex] = selectedAnswerKey;
      }

      currentQuestionIndex = index;
      updateQuestion(currentQuestionIndex);
    });
  });

  // Инициализация первого вопроса
  updateQuestion(currentQuestionIndex);
});
