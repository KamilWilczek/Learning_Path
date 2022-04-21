import React from 'react';
import { NavLink } from 'react-router-dom';
import styles from './HeaderNavigation.module.scss';

const HeaderNavigation = () => (
  <nav>
    <ul className={styles.wrapper}>
      <li className={styles.navItem}><NavLink className={({ isActive }) => (isActive ? styles.navItemLinkActive : styles.navItemLink)} to="/">twitters</NavLink></li>
      <li className={styles.navItem}><NavLink className={({ isActive }) => (isActive ? styles.navItemLinkActive : styles.navItemLink)} to="/articles">articles</NavLink></li>
      <li className={styles.navItem}><NavLink className={({ isActive }) => (isActive ? styles.navItemLinkActive : styles.navItemLink)} to="/notes">notes</NavLink></li>
    </ul>
  </nav>
);

export default HeaderNavigation;  