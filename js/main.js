window.onload = function () {
	get_template("home");
};

let get_template = function (page) {
	let request = new XMLHttpRequest();
	let main_root = document.getElementById("root");
	main_root.innerHTML = "";
	request.open("GET", `pages/${page}.html`);
	request.onload = function () {
		main_root.innerHTML = request.response;
	};
	request.send();
};
