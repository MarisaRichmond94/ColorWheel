import types from '~/sagas/types';

export default class AutoLogoutScheduler {
  constructor(timeInMinutes) {
    this.autoLogoutInterval = null;
    this.autoLogoutModalInterval = null;
    this.timeInMinutes = timeInMinutes;
  }

  initializeAutoLogoutInterval = () => {
    this.autoLogoutInterval = this.startAutoLogoutInterval();
  }

  initializeAutoLogoutModalInterval = () => {
    this.autoLogoutModalInterval = this.startAutoLogoutModalInterval();
  }

  resetAutoLogoutInterval = () => {
    clearInterval(this.autoLogoutInterval);
    clearInterval(this.autoLogoutModalInterval);
    this.autoLogoutInterval = this.startAutoLogoutInterval();
    this.autoLogoutModalInterval = this.startAutoLogoutModalInterval();
  }

  startAutoLogoutInterval = () => {
    return setInterval(() => {
      window.dispatchSagaAction(types.DEAUTHENTICATE_USER);
    }, this.timeInMinutes * 60 * 1000);
  }

  startAutoLogoutModalInterval = () => {
    return setInterval(() => {
      window.dispatchSagaAction(
        types.SET_IS_LOGOUT_WARNING_MODAL_SHOWING,
        { isLogoutWarningModalShowing: true },
      );
    }, (this.timeInMinutes - 1) * 60 * 1000);
  }
}
