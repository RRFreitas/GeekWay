angular.module("app").controller("sideNavCtrl", function (userService, $mdMedia, $mdSidenav, $state, loginService,$mdToast) {

    this.isOpened = true;
    
    this.user = userService.getUser();

    function onErrorCallback(data, status) {
		var _message = '';

		if (!data) {
			_message = 'Ocorreu um erro na comunicação com o servidor, favor chamar o suporte.'
		} else {
			_message = data.mensagem
		}

		$mdToast.show(
			$mdToast.simple()
			.textContent(_message)
			.position('top right')
			.action('OK')
			.hideDelay(6000)
		);
	}
    
    this.title = $state.current.title;

    this.openOrCloseSideNav = function () {
        if($mdMedia('gt-md'))
        this.isOpened = !this.isOpened;
        else
        $mdSidenav('sideNav').toggle()
    }
});