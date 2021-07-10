import React, { createContext, useContext, useState } from 'react';

import types from '~/sagas/types';

const LoginContext = createContext();

const LoginProvider = props => {
  return <LoginContext.Provider value={new UseProvideLogin()} {...props} />;
};

function UseProvideLogin() {
  const [email, setEmail] = useState('');
  const [isSignUpPage, setIsSignUpPage] = useState(false);
  const [isValidEmail, setIsValidEmail] = useState(false);
  const [isValidName, setIsValidName] = useState(false);
  const [isValidPassword, setIsValidPassword] = useState(false);
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');

  const getIsValidInput = type => {
    switch (type) {
      case 'email':
        return isValidEmail;
      case 'name':
        return isValidName;
      case 'password':
        return isValidPassword;
      case 'all':
        return isSignUpPage
          ? isValidName && isValidEmail && isValidPassword
          : isValidEmail && isValidPassword;
      default:
        return false;
    }
  };

  const updateInput = (type, value) => {
    switch (type) {
      case 'email':
        setEmail(value);
        break;
      case 'name':
        setName(value);
        break;
      case 'password':
        setPassword(value);
        break;
      default:
        break;
    }
  };

  const validateInput = (type, value) => {
    switch (type) {
      case 'email':
        validateEmail(value);
        break;
      case 'name':
        validateName(value);
        break;
      case 'password':
        validatePassword(value);
        break;
      default:
        break;
    }
  };

  const validateEmail = email => {
    const validEndings = ['.com', '.org', '.edu', '.gov'];
    const hasOnlyValidCharacters = (
      /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email)
    );
    const hasAtSymbol = email.includes('@');
    const hasValidEnding = validEndings.includes(email.slice(-4));
    setIsValidEmail(hasOnlyValidCharacters && hasAtSymbol && hasValidEnding);
  };

  const validateName = name => {
    const names = name.split(' ');
    const validNames = names.filter(n => n.length > 1);
    setIsValidName(names.length === 2 && validNames.length === 2);
  };

  const validatePassword = password => {
    setIsValidPassword(
      /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{10,}$/.test(password),
    );
  };

  const onFormSubmit = () => {
    window.dispatchSagaAction(types.AUTHENTICATE_USER, { name, email, password });
  };

  const onKeyPress = e => {
    if (e.key === 'Enter') {
      onFormSubmit(e);
    }
  };

  return {
    email,
    isSignUpPage,
    name,
    password,
    getIsValidInput,
    onFormSubmit,
    onKeyPress,
    setIsSignUpPage,
    updateInput,
    validateInput,
  };
}

const useLogin = () => useContext(LoginContext);

export { LoginProvider, useLogin };
