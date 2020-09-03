import React from 'react'
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import { teal, red } from '@material-ui/core/colors';

export default class Config {
  public static theme = createMuiTheme({
    palette: {
      primary: {
        main: teal[500],
      },
      secondary: {
        main: red[500],
      },
    },
  })
}