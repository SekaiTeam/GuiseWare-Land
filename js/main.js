window.onload = function () {

	let template = function () {
		var tmlt = new XMLHttpRequest();
		tmlt.open("GET", "pages/download_launcher.html");
		tmlt.onload = function () {
			document.getElementById("root").innerHTML = tmlt.response;
		};
		tmlt.send();
	};

	template();
};
