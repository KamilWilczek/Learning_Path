import React from "react";
import ListItem from "./ListItem";
import styles from "./List.module.scss";

const List = props => (
  <ul className={styles.wrapper}>
    {props.items.map(item => (
      <ListItem key={item.title} {...item} />
    ))}
  </ul>
);

export default List;
