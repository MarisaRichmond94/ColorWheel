export const keysToCamel = value => {
  if (isObject(value)) {
    const object = {};

    Object.keys(value).forEach(key => {
      object[toCamel(key)] = keysToCamel(value[key]);
    });

    return object;
  } else if (Array.isArray(value)) {
    return value.map(object => {
      return keysToCamel(object);
    });
  }

  return value;
};

export const keysToSnake = value => {
  if (isObject(value)) {
    const object = {};

    Object.keys(value)
      .forEach(key => {
        object[toSnake(key)] = keysToSnake(value[key]);
      });

    return object;
  } else if (Array.isArray(value)) {
    return value.map(object => {
      return keysToSnake(object);
    });
  }

  return value;
};

const isObject = value => {
  return value === Object(value) && !Array.isArray(value) && typeof value !== 'function';
};

const toCamel = string => {
  return string.replace(/([-_][a-z])/ig, ($1) =>
    $1.toUpperCase().replace('-', '').replace('_', '')
  );
};



const toSnake = string => {
  return string
    .replace(/\.?([A-Z]+)/g, (x, y) => '_' + y.toLowerCase())
    .replace(/^_/, '')
    .replace(' ', '');
};
