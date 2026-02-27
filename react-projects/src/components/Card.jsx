import React, { useState, useEffect } from 'react';
import './Card.css';

interface CardProps {
  title: string;
  description: string;
  image?: string;
  onClick?: () => void;
  children?: React.ReactNode;
}

export const Card: React.FC<CardProps> = ({ 
  title, 
  description, 
  image, 
  onClick,
  children 
}) => {
  const [isHovered, setIsHovered] = useState(false);
  const [imageLoaded, setImageLoaded] = useState(false);

  useEffect(() => {
    if (image) {
      const img = new Image();
      img.src = image;
      img.onload = () => setImageLoaded(true);
    }
  }, [image]);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' || e.key === ' ') {
      onClick?.();
    }
  };

  return (
    <div 
      className={`card ${isHovered ? 'card--hovered' : ''}`}
      onClick={onClick}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      onKeyDown={handleKeyDown}
      tabIndex={0}
      role="button"
      aria-label={`Card: ${title}`}
    >
      {image && (
        <div className="card__image-container">
          {imageLoaded ? (
            <img 
              src={image} 
              alt={title} 
              className="card__image" 
            />
          ) : (
            <div className="card__image-placeholder">Loading...</div>
          )}
        </div>
      )}
      
      <div className="card__content">
        <h3 className="card__title">{title}</h3>
        <p className="card__description">{description}</p>
        
        {children && (
          <div className="card__children">
            {children}
          </div>
        )}
      </div>
    </div>
  );
};

export default Card;

