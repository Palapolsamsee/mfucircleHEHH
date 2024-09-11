// static/js/scripts.js

function updateColor(element) {
    const number = parseInt(element.getAttribute('data-number'));
  
    if (number > 30) {
      element.className = 'gold';
    } else if (number > 20) {
      element.className = 'red';
    } else if (number > 10) {
      element.className = 'orange';
    } else if (number >= 0) {
      element.className = 'green';
    } else {
      element.className = '';
    }
  }
  
  // Apply the color update to all like and comment elements
  document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('[id^="likes-"], [id^="comments-"]').forEach(element => {
      updateColor(element);
    });
  });
  
  function likeTweet(tweetId) {
    fetch(`/like_tweet/${tweetId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),  // Ensure CSRF token is sent with the request
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const likeElement = document.getElementById(`likes-${tweetId}`);
            likeElement.textContent = data.likes;
            updateColor(likeElement);  // Update the color based on the new like count
        }
    });
}

// Helper function to get the CSRF token
function likeTweet(tweetId) {
  const likeIcon = document.getElementById(`like-icon-${tweetId}`);
  const likeForm = document.getElementById(`like-form-${tweetId}`);

  fetch(likeForm.action, {
      method: 'POST',
      headers: {
          'X-CSRFToken': likeForm.querySelector('[name=csrfmiddlewaretoken]').value,
      },
  })
  .then(response => response.json())
  .then(data => {
      if (data.liked) {
          likeIcon.innerHTML = '<i class="fa fa-heart" style="color:red;"></i>';
      } else {
          likeIcon.innerHTML = '<i class="fa fa-heart" style="color:black;"></i>';
      }
      document.getElementById(`likes-${tweetId}`).textContent = data.like_count;
  })
  .catch(error => console.error('Error:', error));
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


document.addEventListener('DOMContentLoaded', function () {
    const openButton = document.getElementById('open-popup');
    const closeButton = document.getElementById('close-popup');
    const popup = document.getElementById('popup-form');

    openButton.addEventListener('click', function () {
        popup.classList.add('active');
    });

    closeButton.addEventListener('click', function () {
        popup.classList.remove('active');
    });

    // Optional: Close popup when clicking outside of it
    document.addEventListener('click', function (event) {
        if (!popup.contains(event.target) && !openButton.contains(event.target)) {
            popup.classList.remove('active');
        }
    });
});