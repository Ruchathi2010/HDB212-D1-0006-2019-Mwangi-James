import React from 'react';
import { Box, Heading, VStack, HStack, Text } from '@chakra-ui/react';

function AdsList() {
  const ads = [
    { id: 1, title: 'Ad 1', status: 'Active' },
    { id: 2, title: 'Ad 2', status: 'Pending' },
  ];

  return (
    <Box bg="white" p={4} rounded="md" shadow="md">
      <Heading size="md" mb={4}>
        Ads List
      </Heading>
      <VStack spacing={2} align="stretch">
        {ads.map((ad) => (
          <HStack
            key={ad.id}
            justifyContent="space-between"
            p={2}
            borderBottom="1px solid"
            borderColor="gray.200"
          >
            <Text>{ad.title}</Text>
            <Text fontWeight="bold">{ad.status}</Text>
          </HStack>
        ))}
      </VStack>
    </Box>
  );
}

export default AdsList;
