import React, { useState, useCallback } from 'react';
import './Button.css';

const Button = ({ 
  children, 
  variant = 'primary', 
  size = 'medium',
  disabled = false,
  loading = false,
  onClick,
  type = 'button',
  className = ''
}) => {
  const [isPressed, setIsPressed] = useState(false);

  const handleClick = useCallback((e) => {
    if (!disabled && !loading && onClick) {
      onClick(e);
    }
  }, [disabled, loading, onClick]);

  const handleMouseDown = () => {
    setIsPressed(true);
  };

  const handleMouseUp = () => {
    setIsPressed(false);
  };

  const buttonClasses = [
    'button',
    `button--${variant}`,
    `button--${size}`,
    isPressed ? 'button--pressed' : '',
    loading ? 'button--loading' : '',
    disabled ? 'button--disabled' : '',
    className
  ].filter(Boolean).join(' ');

  return (
    <button
      type={type}
      className={buttonClasses}
      disabled={disabled || loading}
      onClick={handleClick}
      onMouseDown={handleMouseDown}
      onMouseUp={handleMouseUp}
      onMouseLeave={handleMouseUp}
    >
      {loading && (
        <span className="button__spinner">
          <svg viewBox="0 0 24 24" className="button__spinner-icon">
            <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="3" fill="none" strokeDasharray="31.4" strokeDashoffset="10" />
          </svg>
        </span>
      )}
      <span className={loading ? 'button__content--hidden' : 'button__content'}>
        {children}
      </span>
    </button>
  );
};

export default Button;

