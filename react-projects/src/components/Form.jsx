import React, { useState, useCallback } from 'react';
import './Form.css';

const Form = ({ onSubmit, children, className = '' }) => {
  const handleSubmit = useCallback((e) => {
    e.preventDefault();
    if (onSubmit) {
      const formData = new FormData(e.target);
      const data = Object.fromEntries(formData.entries());
      onSubmit(data);
    }
  }, [onSubmit]);

  return (
    <form onSubmit={handleSubmit} className={`form ${className}`}>
      {children}
    </form>
  );
};

const Input = ({ 
  label, 
  name, 
  type = 'text', 
  placeholder, 
  defaultValue,
  required = false,
  error,
  onChange 
}) => {
  const [value, setValue] = useState(defaultValue || '');
  const [touched, setTouched] = useState(false);

  const handleChange = (e) => {
    const newValue = e.target.value;
    setValue(newValue);
    if (onChange) {
      onChange(name, newValue);
    }
  };

  const handleBlur = () => {
    setTouched(true);
  };

  const hasError = touched && error;

  return (
    <div className={`form-group ${hasError ? 'form-group--error' : ''}`}>
      {label && <label htmlFor={name} className="form-label">{label}</label>}
      <input
        id={name}
        name={name}
        type={type}
        value={value}
        placeholder={placeholder}
        required={required}
        onChange={handleChange}
        onBlur={handleBlur}
        className="form-input"
      />
      {hasError && <span className="form-error">{error}</span>}
    </div>
  );
};

const Textarea = ({ 
  label, 
  name, 
  placeholder, 
  defaultValue,
  rows = 4,
  required = false,
  error 
}) => {
  const [value, setValue] = useState(defaultValue || '');
  const [touched, setTouched] = useState(false);

  const handleChange = (e) => {
    setValue(e.target.value);
  };

  const handleBlur = () => {
    setTouched(true);
  };

  const hasError = touched && error;

  return (
    <div className={`form-group ${hasError ? 'form-group--error' : ''}`}>
      {label && <label htmlFor={name} className="form-label">{label}</label>}
      <textarea
        id={name}
        name={name}
        value={value}
        placeholder={placeholder}
        rows={rows}
        required={required}
        onChange={handleChange}
        onBlur={handleBlur}
        className="form-textarea"
      />
      {hasError && <span className="form-error">{error}</span>}
    </div>
  );
};

const Select = ({ 
  label, 
  name, 
  options = [], 
  defaultValue,
  required = false,
  error 
}) => {
  const [value, setValue] = useState(defaultValue || '');

  return (
    <div className="form-group">
      {label && <label htmlFor={name} className="form-label">{label}</label>}
      <select
        id={name}
        name={name}
        value={value}
        required={required}
        onChange={(e) => setValue(e.target.value)}
        className="form-select"
      >
        <option value="">Select an option</option>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      {error && <span className="form-error">{error}</span>}
    </div>
  );
};

const Checkbox = ({ 
  label, 
  name, 
  defaultChecked = false 
}) => {
  const [checked, setChecked] = useState(defaultChecked);

  return (
    <div className="form-group form-group--checkbox">
      <input
        id={name}
        name={name}
        type="checkbox"
        checked={checked}
        onChange={(e) => setChecked(e.target.checked)}
        className="form-checkbox"
      />
      {label && <label htmlFor={name} className="form-label">{label}</label>}
    </div>
  );
};

const RadioGroup = ({ 
  label, 
  name, 
  options = [], 
  defaultValue 
}) => {
  const [value, setValue] = useState(defaultValue || '');

  return (
    <div className="form-group">
      {label && <label className="form-label">{label}</label>}
      <div className="form-radio-group">
        {options.map((option) => (
          <label key={option.value} className="form-radio-label">
            <input
              type="radio"
              name={name}
              value={option.value}
              checked={value === option.value}
              onChange={(e) => setValue(e.target.value)}
              className="form-radio"
            />
            {option.label}
          </label>
        ))}
      </div>
    </div>
  );
};

Form.Input = Input;
Form.Textarea = Textarea;
Form.Select = Select;
Form.Checkbox = Checkbox;
Form.RadioGroup = RadioGroup;

export default Form;

