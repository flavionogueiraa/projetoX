export default function globalAnimations() {
	const axis = {
		x: {
			x: 0,
		},
		y: {
			y: 0,
		},
	};

	function animateSideBar() {
		const sideBarSelector = ".sidebar > ul > li, .sidebar > a ";
		const sideBar = document.querySelector(sideBarSelector);

		sideBar &&
			gsap.set(sideBarSelector, {
				opacity: 0,
				y: 50,
				transition: "initial",
			});

		sideBar &&
			document.addEventListener("DOMContentLoaded", () => {
				defaultAnimation(sideBarSelector, axis.y);
			});
	}

	function animateBreadcrumb() {
		const breadcrumbSelector = ".breadcrumb-wrapper li";
		const breadcrumbs = document.querySelectorAll(breadcrumbSelector);

		const tl = gsap.timeline()
		breadcrumbs.forEach((breadcrumb) => animateItemBreadcrumb(breadcrumb));

		function animateItemBreadcrumb(breadcrumb) {
			tl.from(breadcrumb, {
				x: -50,
				opacity: 0,
				duration: 0.15,
			})
		}
	}

	function animateNotificacaoButton() {
		const NotificacaoButtonSelector = ".botao-notificacao";
		const NotificacaoButton = document.querySelector(NotificacaoButtonSelector);

		NotificacaoButton &&
			gsap.set(NotificacaoButtonSelector, {
				opacity: 0,
				x: 150,
				transition: "initial",
			});

		NotificacaoButton &&
			document.addEventListener("DOMContentLoaded", () => {
				defaultAnimation(NotificacaoButtonSelector, axis.x);
			});
	}

	function animateMainContent() {
		const mainContentSelector = ".container-content > *";
		const mainContent = document.querySelector(mainContentSelector);

		mainContent &&
			gsap.set(mainContentSelector, {
				opacity: 0,
				y: 50,
				transition: "initial",
			});

		mainContent &&
			document.addEventListener("DOMContentLoaded", () => {
				defaultAnimation(mainContentSelector, axis.y);
			});
	}

	function defaultAnimation(selector, axis) {
		gsap.to(selector, {
			opacity: 1,
			stagger: 0.05,
			ease: "sine",
			clearProps: "all",
			...axis,
		});
	}

	(function init() {
		animateSideBar();
		animateBreadcrumb();
		animateNotificacaoButton();
		animateMainContent();
	})();
}
