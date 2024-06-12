$(".menu > ul > li").click(function (e) {
  $(this).siblings().removeClass("active");
  $(this).toggleClass("active");

  $(this).find("ul").slideToggle();
  $(this).siblings().find("ul").slideUp();
  $(this).siblings().find("ul").find("li").removeClass("active");
});

$(".menu-btn").click(function () {
  $(".sidebar").toggleClass("active");
});

const logoutBtn = document.getElementById("logoutBtn");

logoutBtn.addEventListener("click", () => {
  eel.Logout()(function(result) {
    if (result && typeof result === 'string' && result.startsWith('Error')) {
      alert('Logout failed: ' + result);
    } else {
      window.location.href = 'M_Login.html';
    }
  });
});