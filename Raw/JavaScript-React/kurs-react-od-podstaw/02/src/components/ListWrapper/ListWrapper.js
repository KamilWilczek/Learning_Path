import React from 'react'
import ListItem from '../ListItem/Listitem'
import './ListWrapper.css'
import { twitterAccounts } from '../../data/twitterAccounts'

const ListWrapper = () => (
  <ul className="listWrapper__wrapper">
    {twitterAccounts.map((item) => (
      <ListItem key={item.name} {...item} />
    ))}
  </ul>
)

export default ListWrapper
