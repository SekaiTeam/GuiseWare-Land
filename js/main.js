window.onload = function () {
	get_template("home");
};

let get_template = function (page) {
	let request = new XMLHttpRequest();
	let main_root = document.getElementById("root");
	main_root.innerHTML = `<span class="rotating_loader" />`;
	request.open("GET", `pages/${page}.html`);
	request.onload = function () {
		main_root.innerHTML = request.response;
	};
	request.send();
};

let activate = function (target) {
	document.querySelectorAll("button[selected]").forEach(function(element,index) {
		element.removeAttribute("selected");
	});
	let attribute = document.getElementsByName(target.getAttribute("name"))[1]
	attribute.setAttribute("selected",'')
	target.setAttribute("selected",'');
}