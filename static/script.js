const chatForm = document.getElementById('chat-form');
const chatMessageInput = document.getElementById('chat-message');
const chatMessagesContainer = document.querySelector('.chat-messages');
const loadingAnimation = document.querySelector('.loading-animation');
const loremIpsumAPI = 'https://baconipsum.com/api/?type=all-meat&sentences=1';

chatForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const messageText = chatMessageInput.value.trim();

  if (messageText === '') {
    return;
  }

  const message = createMessage(messageText, 'sent');
  chatMessagesContainer.insertBefore(message, loadingAnimation);
  loadingAnimation.style.display = 'flex';

  // fetch(loremIpsumAPI)
  fetch(' http://127.0.0.1:5000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin':'no-cors'
      },
      // mode: "no-cors",
      // referrerPolicy: "no-referrer",
      body: JSON.stringify({
        message:messageText
      })
    })
    .then((response) => response.json())
    .then((data) => {
      const replyText = data['response'];
      const replyMessage = createMessage(replyText, 'received');
      chatMessagesContainer.insertBefore(replyMessage, loadingAnimation);
      chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
    })
    .catch((error) => {
      console.error(error);
    })
    .finally(() => {
      loadingAnimation.style.display = 'none'; // Hide loading animation
    });

  chatMessageInput.value = '';
  chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
});

function createMessage(text, messageType) {
  const message = document.createElement('div');
  message.classList.add('message', messageType);

  const messageText = document.createElement('p');
  messageText.textContent = text;
  message.appendChild(messageText);

  const messageTime = document.createElement('span');
  messageTime.classList.add('time');
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  messageTime.textContent = `${hours}:${minutes}`;
  message.appendChild(messageTime);

  return message;
}

function openTab(event, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  event.currentTarget.className += " active";
}

// Set the default tab to open on page load
document.getElementById("tab1").style.display = "block";
document.getElementsByClassName("tablinks")[0].className += " active";