
// src/components/Header.js
import React from 'react';
import { Box, Image, Flex, Text } from '@chakra-ui/react';

function Header() {
  return (
    <Flex
      as="header"
      align="center"
      justify="space-between"
      bg="blue.800"
      color="white"
      padding="4"
      boxShadow="md"
    >
      {/* Logo */}
      <Flex align="center">
        <Image
          src="/kbc-logo.png"
          alt="KBC Logo"
          boxSize="50px"
          objectFit="contain"
          marginRight="3"
        />
        <Text fontSize="xl" fontWeight="bold">
          KBC Advertising Management System
        </Text>
      </Flex>

      {/* Optional right-side info */}
      <Box>
        {/* You can add user profile, notifications, etc. here */}
      </Box>
    </Flex>
  );
}

export default Header;
