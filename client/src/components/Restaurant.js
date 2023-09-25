import React from "react";

export default function Restaurant({ id, name, ingredients, image, price }) {
  // console.log(id,name,address);
  return (
    <div class="card">
      <img src={image} class="card-img" alt="" />
      <div class="card-body">
        <div className="pizza_name">
          <h1 class="card-title">{name}</h1>
          <h1 class="card-price">{price}</h1>
        </div>
        <p class="card-sub-title">{}</p>
        <p class="card-info">{ingredients}</p>
        <div className="btn-div">
          <button class="card-btn">order</button>
        </div>
      </div>
    </div>
  );
}
