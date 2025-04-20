document.addEventListener('DOMContentLoaded', () => {
  const newTaskInput = document.getElementById('new-task');
  const addTaskBtn = document.getElementById('add-task-btn');
  const taskList = document.getElementById('task-list');
  let tasks = [];

  function renderTasks() {
    taskList.innerHTML = '';
    tasks.forEach(task => {
      const li = document.createElement('li');
      li.className = 'task-item';
      if (task.completed) li.classList.add('completed');

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.checked = task.completed;
      checkbox.addEventListener('change', () => {
        toggleTask(task.id);
      });

      const span = document.createElement('span');
      span.className = 'task-text';
      span.textContent = task.text;

      const deleteBtn = document.createElement('button');
      deleteBtn.className = 'delete-btn';
      deleteBtn.textContent = '✕';
      deleteBtn.addEventListener('click', () => {
        deleteTask(task.id);
      });

      li.appendChild(checkbox);
      li.appendChild(span);
      li.appendChild(deleteBtn);
      taskList.appendChild(li);
    });
  }

  function addTask() {
    const text = newTaskInput.value.trim();
    if (text === '') return;
    const task = { id: Date.now(), text, completed: false };
    tasks.push(task);
    newTaskInput.value = '';
    renderTasks();
  }

  function toggleTask(id) {
    const task = tasks.find(t => t.id === id);
    if (task) {
      task.completed = !task.completed;
      renderTasks();
    }
  }

  function deleteTask(id) {
    tasks = tasks.filter(t => t.id !== id);
    renderTasks();
  }

  addTaskBtn.addEventListener('click', addTask);
  newTaskInput.addEventListener('keypress', e => {
    if (e.key === 'Enter') addTask();
  });

  renderTasks();
});